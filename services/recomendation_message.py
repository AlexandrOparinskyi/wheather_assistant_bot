from typing import Dict, Any, List


def format_recommendation_message(weather_data: Dict[str, Any],
                                  recommendations: Dict[str, List]) -> str:
    """
    Форматирует краткое сообщение с рекомендациями
    """
    temp_icon = _get_temperature_icon(weather_data['avg_temp'])
    day_analysis = weather_data.get('day_analysis', {})

    # Заголовок
    if day_analysis.get('is_big_difference'):
        title = f"🔄 РЕКОМЕНДАЦИИ НА ДЕНЬ С БОЛЬШИМ ПЕРЕПАДОМ ТЕМПЕРАТУР"
    else:
        title = f"{temp_icon} РЕКОМЕНДАЦИИ ПО ОДЕЖДЕ НА СЕГОДНЯ"

    message = f"""
{title}
📍 {weather_data['location']} • {weather_data['date']}

🌡️ ТЕМПЕРАТУРНЫЙ РЕЖИМ ДНЯ:
{_format_day_temperature_analysis(day_analysis)}

🎯 СТРАТЕГИЯ НА ДЕНЬ:
{_format_list(recommendations['day_strategy'])}

🧥 ЧТО ОДЕТЬ (ОСНОВНОЕ):
👒 Головной убор: {_format_first_items(recommendations['headwear'])}
👚 Верх (многослойность): {_format_first_items(recommendations['upper_body'])}
👖 Низ: {_format_first_items(recommendations['lower_body'])}
👟 Обувь: {_format_first_items(recommendations['footwear'])}

💡 ВАЖНО: {_format_important_tips(recommendations['important_tips'])}
"""

    return message.strip()


def _format_important_tips(items: list, max_items: int = 3):
    if not items:
        return "стандартный вариант"
    return "\n" + "\n".join(items[:max_items])


def _format_first_items(items: list, max_items: int = 3) -> str:
    """Форматирует только первые несколько элементов"""
    if not items:
        return "стандартный вариант"
    return ", ".join(items[:max_items])


def _format_day_temperature_analysis(day_analysis: Dict) -> str:
    """Форматирует анализ температуры по времени суток"""
    if not day_analysis:
        return "• Данные о изменении температуры временно недоступны"

    morning = day_analysis.get('morning', {})
    day = day_analysis.get('day', {})
    evening = day_analysis.get('evening', {})

    lines = [
        f"• 🌅 Утро (6-10ч): {morning.get('avg_temp', 0):.1f}°C - {morning.get('condition', 'Неизвестно')}",
        f"• ☀️ День (11-16ч): {day.get('avg_temp', 0):.1f}°C - {day.get('condition', 'Неизвестно')}",
        f"• 🌇 Вечер (17-21ч): {evening.get('avg_temp', 0):.1f}°C - {evening.get('condition', 'Неизвестно')}",
    ]

    if day_analysis.get('temp_difference', 0) > 5:
        lines.append(
            f"• 🔄 Перепад температур: +{day_analysis['temp_difference']:.1f}°C в течение дня")

    if day_analysis.get('is_big_difference'):
        lines.append("• ⚠️ Большой перепад! Одевайтесь слоями")

    return "\n".join(lines)


def _format_list(items: list) -> str:
    """Форматирует список в виде пунктов"""
    if not items:
        return "• стандартный вариант"
    return "\n".join([f"• {item}" for item in items])


def _format_hourly_forecast(forecast: list) -> str:
    """Форматирует почасовой прогноз"""
    if not forecast:
        return "• данные временно недоступны"

    lines = []
    for hour in forecast:
        rain_icon = " ☔" if hour['chance_of_rain'] > 50 else ""
        lines.append(
            f"• {hour['time']}: {hour['temp']}°C, {hour['condition']}{rain_icon}")
    return "\n".join(lines)


def _get_temperature_icon(temp: float) -> str:
    """Возвращает иконку для температуры с расширенными диапазонами"""
    if temp < -20: return "🥶🌡️"
    elif temp < -10: return "🥶"
    elif temp < -5: return "❄️🧊"
    elif temp < 0: return "❄️"
    elif temp <= 5: return "🌨️"
    elif temp <= 10: return "🌫️"
    elif temp <= 15: return "🌤️"
    elif temp <= 19: return "😊"
    elif temp <= 24: return "☀️"
    elif temp <= 29: return "🔥"
    else: return "🌡️🔥"


def _get_weather_icon(condition: str) -> str:
    """Возвращает иконку для погодных условий"""
    condition_lower = condition.lower()
    if 'дождь' in condition_lower or 'ливень' in condition_lower:
        return "🌧️"
    elif 'гроза' in condition_lower:
        return "⛈️"
    elif 'снег' in condition_lower:
        return "❄️"
    elif 'туман' in condition_lower:
        return "🌫️"
    elif 'облачно' in condition_lower:
        return "☁️"
    elif 'ясно' in condition_lower or 'солнечно' in condition_lower:
        return "☀️"
    else:
        return "🌤️"


def _get_rain_icon(chance: int) -> str:
    """Возвращает иконку для вероятности дождя"""
    if chance > 80:
        return "⛈️"
    elif chance > 50:
        return "🌧️"
    elif chance > 20:
        return "☔"
    else:
        return ""


def _get_uv_icon(uv: float) -> str:
    """Возвращает иконку для УФ-индекса"""
    if uv > 8:
        return "⚠️"
    elif uv > 6:
        return "🔆"
    elif uv > 3:
        return "😎"
    else:
        return ""