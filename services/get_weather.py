import aiohttp
from typing import Dict, Any, List
from datetime import datetime


async def get_weather_data(city: str) -> Dict[str, Any]:
    """
    Получает данные о погоде от API с почасовым прогнозом
    """
    url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        'key': 'b37226ed91f5447192a185002252409',
        'q': city,
        'lang': 'ru',
        'days': 1,
        'hours': 24  # Получаем данные на все 24 часа
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()

                    # Основные данные
                    current = data['current']
                    forecast_day = data['forecast']['forecastday'][0]['day']
                    location = data['location']
                    hours = data['forecast']['forecastday'][0]['hour']

                    # Анализ температуры в течение дня
                    day_analysis = _analyze_day_temperature(hours)

                    return {
                        'success': True,
                        'location': location['name'],
                        'date': data['forecast']['forecastday'][0]['date'],
                        'timestamp': datetime.now().isoformat(),

                        # Основные погодные параметры
                        'avg_temp': forecast_day['avgtemp_c'],
                        'max_temp': forecast_day['maxtemp_c'],
                        'min_temp': forecast_day['mintemp_c'],
                        'condition': forecast_day['condition']['text'],
                        'chance_of_rain': forecast_day['daily_chance_of_rain'],
                        'wind_speed': forecast_day['maxwind_kph'],
                        'uv_index': forecast_day['uv'],

                        # Дополнительная информация
                        'current_temp': current['temp_c'],
                        'feels_like': current['feelslike_c'],
                        'humidity': current['humidity'],
                        'sunrise': data['forecast']['forecastday'][0]['astro'][
                            'sunrise'],
                        'sunset': data['forecast']['forecastday'][0]['astro'][
                            'sunset'],

                        # Почасовой прогноз
                        'hourly_forecast': _get_key_hours_forecast(hours),

                        # Анализ дня
                        'day_analysis': day_analysis,
                        'all_hours': hours  # Все часы для детального анализа
                    }
                else:
                    return {
                        'success': False,
                        'error': f"Ошибка API: {response.status}"
                    }

    except Exception as e:
        return {
            'success': False,
            'error': f"Ошибка соединения: {str(e)}"
        }


def _analyze_day_temperature(hours: List[Dict]) -> Dict[str, Any]:
    """Анализирует изменение температуры в течение дня"""
    if not hours:
        return {}

    # Находим ключевые периоды дня
    morning_hours = [hour for hour in hours if
                     6 <= int(hour['time'][11:13]) <= 10]
    day_hours = [hour for hour in hours if 11 <= int(hour['time'][11:13]) <= 16]
    evening_hours = [hour for hour in hours if
                     17 <= int(hour['time'][11:13]) <= 21]
    night_hours = [hour for hour in hours if
                   22 <= int(hour['time'][11:13]) or int(
                       hour['time'][11:13]) <= 5]

    # Температуры по периодам
    morning_temps = [hour['temp_c'] for hour in
                     morning_hours] if morning_hours else [0]
    day_temps = [hour['temp_c'] for hour in day_hours] if day_hours else [0]
    evening_temps = [hour['temp_c'] for hour in
                     evening_hours] if evening_hours else [0]

    # Анализ перепадов
    temp_difference = max(day_temps) - min(
        morning_temps) if morning_temps and day_temps else 0

    return {
        'morning': {
            'min_temp': min(morning_temps) if morning_temps else 0,
            'max_temp': max(morning_temps) if morning_temps else 0,
            'avg_temp': sum(morning_temps) / len(
                morning_temps) if morning_temps else 0,
            'condition': morning_hours[0]['condition'][
                'text'] if morning_hours else 'Неизвестно'
        },
        'day': {
            'min_temp': min(day_temps) if day_temps else 0,
            'max_temp': max(day_temps) if day_temps else 0,
            'avg_temp': sum(day_temps) / len(day_temps) if day_temps else 0,
            'condition': day_hours[0]['condition'][
                'text'] if day_hours else 'Неизвестно'
        },
        'evening': {
            'min_temp': min(evening_temps) if evening_temps else 0,
            'max_temp': max(evening_temps) if evening_temps else 0,
            'avg_temp': sum(evening_temps) / len(
                evening_temps) if evening_temps else 0,
            'condition': evening_hours[0]['condition'][
                'text'] if evening_hours else 'Неизвестно'
        },
        'temp_difference': temp_difference,
        'is_big_difference': temp_difference > 8,
        # Большой перепад если больше 8 градусов
        'warming_trend': max(day_temps) > max(
            morning_temps) if morning_temps and day_temps else False,
        'cooling_trend': min(evening_temps) < max(
            day_temps) if day_temps and evening_temps else False
    }


def _get_key_hours_forecast(hours: list) -> list:
    """Внутренняя функция для получения прогноза по ключевым часам"""
    key_hours = [6, 8, 10, 12, 14, 16, 18, 20, 22]  # Более детальный прогноз
    result = []

    for hour_idx in key_hours:
        if hour_idx < len(hours):
            hour = hours[hour_idx]
            result.append({
                'time': hour['time'][11:16],
                'temp': hour['temp_c'],
                'condition': hour['condition']['text'],
                'chance_of_rain': hour['chance_of_rain'],
                'feels_like': hour['feelslike_c']
            })

    return result
