from .get_weather import get_weather_data
from .get_clothing import generate_clothing_recommendations
from .recomendation_message import format_recommendation_message

__all__ = [
    'get_weather_data',
    'generate_clothing_recommendations',
    'format_recommendation_message',
    'get_weather_recommendation_message'
]


async def get_weather_recommendation_message(city: str) -> str:
    """
    Главная функция: получает погоду и возвращает готовое сообщение с рекомендациями
    """
    # Получаем данные о погоде
    weather_data = await get_weather_data(city)

    if not weather_data['success']:
        return f"❌ Не удалось получить погоду для {city}: {weather_data['error']}"

    # Генерируем рекомендации по одежде с учетом дня
    recommendations = generate_clothing_recommendations(
        avg_temp=weather_data['avg_temp'],
        condition=weather_data['condition'],
        chance_of_rain=weather_data['chance_of_rain'],
        wind_speed=weather_data['wind_speed'],
        uv_index=weather_data['uv_index'],
        day_analysis=weather_data.get('day_analysis')  # Передаем анализ дня
    )

    # Форматируем и возвращаем готовое сообщение
    return format_recommendation_message(weather_data, recommendations)
