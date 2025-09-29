from typing import Dict, Any, List


def format_recommendation_message(weather_data: Dict[str, Any],
                                  recommendations: Dict[str, List]) -> str:
    """
    Форматирует сообщение с акцентом на утренние рекомендации
    """
    day_analysis = weather_data.get('day_analysis', {})
    morning_temp = day_analysis.get('morning', {}).get('avg_temp', weather_data['avg_temp'])

    temp_icon = _get_temperature_icon(morning_temp)

    # Определяем тип дня для заголовка
    temp_diff = day_analysis.get('day', {}).get('avg_temp', 0) - morning_temp
    if temp_diff > 10:
        title = f"🔄 СЕГОДНЯ: УТРОМ ХОЛОДНО → ДНЕМ ТЕПЛО"
    elif temp_diff > 5:
        title = f"📊 СЕГОДНЯ: УТРОМ ПРОХЛАДНО → ДНЕМ КОМФОРТНО"
    else:
        title = f"{temp_icon} ЧТО ОДЕТЬ СЕГОДНЯ"

    message = f"""
{title}
📍 {weather_data['location']} • {weather_data['date']}

🌡️ ПОГОДА ПО ВРЕМЕНИ СУТОК:
{_format_day_temperature_analysis(day_analysis)}

🎯 СЕГОДНЯ ВАЖНО:
{_format_list(recommendations['day_strategy'])}

👕 КОМПЛЕКТ ОДЕЖДЫ:
• Головной убор: {_format_first_items(recommendations['headwear'])}
• Верх: {_format_first_items(recommendations['upper_body'], 5)}
• Низ: {_format_first_items(recommendations['lower_body'], 5)}
• Обувь: {_format_first_items(recommendations['footwear'], 5)}

📌 ПОЛЕЗНЫЕ СОВЕТЫ:
{_format_important_tips(recommendations['important_tips'])}
"""

    return message.strip()


def _format_important_tips(items: list) -> str:
    """Форматирует важные советы"""
    if not items:
        return "• Стандартные рекомендации подходят для сегодняшней погоды"

    formatted = []
    for item in items[:4]:
        formatted.append(f"• {item}")
    return "\n".join(formatted)


def _format_day_temperature_analysis(day_analysis: Dict) -> str:
    """Форматирует анализ температуры с акцентом на утро"""
    if not day_analysis:
        return "• Данные о изменении температуры временно недоступны"

    morning = day_analysis.get('morning', {})
    day = day_analysis.get('day', {})
    evening = day_analysis.get('evening', {})

    lines = [
        f"• 🌅 УТРО (6-10): {morning.get('avg_temp', 0):.0f}°C, {morning.get('condition', 'Неизвестно')}",
        f"• ☀️ ДЕНЬ (11-16): {day.get('avg_temp', 0):.0f}°C, {day.get('condition', 'Неизвестно')}",
        f"• 🌇 ВЕЧЕР (17-21): {evening.get('avg_temp', 0):.0f}°C, {evening.get('condition', 'Неизвестно')}",
    ]

    temp_diff = day.get('avg_temp', 0) - morning.get('avg_temp', 0)
    if temp_diff > 8:
        lines.append(f"• 📈 Перепад: +{temp_diff:.0f}°C - утром нужна куртка, днем можно без")
    elif temp_diff > 5:
        lines.append(f"• 📈 Перепад: +{temp_diff:.0f}°C - учитывайте при выборе одежды")

    return "\n".join(lines)


def _format_first_items(items: list, max_items: int = 3) -> str:
    """Форматирует только первые несколько элементов"""
    if not items:
        return "по погоде"
    return ", ".join(items[:max_items])


def _format_list(items: list) -> str:
    """Форматирует список в виде пунктов"""
    if not items:
        return "• Стандартные рекомендации"
    return "\n".join([f"• {item}" for item in items])


def _get_temperature_icon(temp: float) -> str:
    """Возвращает иконку для УТРЕННЕЙ температуры"""
    if temp < -20:
        return "🥶"
    elif temp < -10:
        return "❄️"
    elif temp < -3:
        return "🧊"
    elif temp < 3:
        return "🌨️"
    elif temp < 8:
        return "🌫️"
    elif temp < 13:
        return "🌤️"
    elif temp < 18:
        return "😊"
    elif temp < 23:
        return "☀️"
    elif temp < 28:
        return "🔥"
    else:
        return "🌡️"
