import asyncio
import aiohttp


async def get_weather_openweather():
    url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        'key': 'b37226ed91f5447192a185002252409',
        'q': "Москва",
        'lang': 'ru',
        'days': 1
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()

                # Извлекаем данные
                location = data['location']
                current = data['current']
                forecast_day = data['forecast']['forecastday'][0]['day']
                astro = data['forecast']['forecastday'][0]['astro']
                hours = data['forecast']['forecastday'][0]['hour']

                # Выводим основную информацию
                print("=" * 50)
                print(f"🌤 ПОГОДА В {location['name'].upper()}")
                print("=" * 50)

                # Текущая погода
                print("\n📊 ТЕКУЩАЯ ПОГОДА:")
                print(f"• Время: {location['localtime']}")
                print(
                    f"• Температура: {current['temp_c']}°C (ощущается как {current['feelslike_c']}°C)")
                print(f"• Погода: {current['condition']['text']}")
                print(
                    f"• Ветер: {current['wind_kph']} км/ч, направление: {current['wind_dir']}")
                print(f"• Влажность: {current['humidity']}%")
                print(f"• Давление: {current['pressure_mb']} мбар")
                print(f"• Видимость: {current['vis_km']} км")
                print(f"• УФ-индекс: {current['uv']}")

                # Прогноз на день
                print("\n📅 ПРОГНОЗ НА ДЕНЬ:")
                print(f"• Дата: {data['forecast']['forecastday'][0]['date']}")
                print(f"• Макс. температура: {forecast_day['maxtemp_c']}°C")
                print(f"• Мин. температура: {forecast_day['mintemp_c']}°C")
                print(f"• Средняя температура: {forecast_day['avgtemp_c']}°C")
                print(f"• Погода: {forecast_day['condition']['text']}")
                print(f"• Макс. ветер: {forecast_day['maxwind_kph']} км/ч")
                print(f"• Осадки: {forecast_day['totalprecip_mm']} мм")
                print(
                    f"• Вероятность дождя: {forecast_day['daily_chance_of_rain']}%")
                print(
                    f"• Вероятность снега: {forecast_day['daily_chance_of_snow']}%")
                print(f"• Средняя влажность: {forecast_day['avghumidity']}%")
                print(f"• УФ-индекс: {forecast_day['uv']}")

                # Астрономические данные
                print("\n🌙 АСТРОНОМИЯ:")
                print(f"• Восход солнца: {astro['sunrise']}")
                print(f"• Закат солнца: {astro['sunset']}")
                print(f"• Восход луны: {astro['moonrise']}")
                print(f"• Закат луны: {astro['moonset']}")
                print(f"• Фаза луны: {astro['moon_phase']}")

                # Почасовой прогноз (ключевые часы)
                print("\n⏰ ПОЧАСОВОЙ ПРОГНОЗ (ключевые часы):")
                key_hours = [0, 6, 9, 12, 15, 18, 21]  # Важные часы дня
                for hour_idx in key_hours:
                    if hour_idx < len(hours):
                        hour = hours[hour_idx]
                        print(
                            f"• {hour['time'][11:16]}: {hour['temp_c']}°C, {hour['condition']['text']}, "
                            f"дождь: {hour['chance_of_rain']}%")

                # Экстремальные значения за день
                print("\n📈 ЭКСТРЕМУМЫ ДНЯ:")
                temps = [hour['temp_c'] for hour in hours]
                rains = [hour['chance_of_rain'] for hour in hours]
                print(f"• Самая высокая температура: {max(temps)}°C")
                print(f"• Самая низкая температура: {min(temps)}°C")
                print(f"• Макс. вероятность дождя: {max(rains)}%")

                # Рекомендации
                print("\n💡 РЕКОМЕНДАЦИИ:")
                if forecast_day['daily_chance_of_rain'] > 50:
                    print("• Возьмите зонт! ☔")
                if current['uv'] > 5:
                    print("• Используйте солнцезащитный крем! ☀️")
                if forecast_day['maxwind_kph'] > 20:
                    print("• Одевайтесь теплее, ветрено! 💨")
                if forecast_day['avgtemp_c'] < 10:
                    print("• Оденьтесь теплее! 🧥")
                elif forecast_day['avgtemp_c'] > 25:
                    print("• Оденьтесь легче! 👕")

            else:
                print(f"Ошибка API: {response.status}")


asyncio.run(get_weather_openweather())
