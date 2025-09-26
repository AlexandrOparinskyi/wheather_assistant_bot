from typing import Dict, List


def generate_clothing_recommendations(avg_temp: float, condition: str,
                                      chance_of_rain: int, wind_speed: float,
                                      uv_index: float,
                                      day_analysis: Dict = None) -> Dict[
    str, List]:
    """
    Генерирует рекомендации по одежде с учетом изменения температуры в течение дня
    """
    recommendations = {
        'headwear': [],
        'upper_body': [],
        'lower_body': [],
        'footwear': [],
        'accessories': [],
        'important_tips': [],
        'day_strategy': []  # Новая категория - стратегия на день
    }

    # Базовые рекомендации по средней температуре
    _add_base_recommendations(recommendations, avg_temp)

    # Рекомендации с учетом изменения температуры в течение дня
    if day_analysis and day_analysis.get('temp_difference', 0) > 0:
        _add_day_strategy_recommendations(recommendations, day_analysis)

    # Рекомендации по осадкам, ветру и солнцу
    _add_weather_recommendations(recommendations, condition, chance_of_rain,
                                 wind_speed, uv_index)

    # Убираем дубликаты
    for category in recommendations:
        recommendations[category] = list(
            dict.fromkeys(recommendations[category]))

    return recommendations


def _add_base_recommendations(recommendations: Dict[str, List],
                              avg_temp: float):
    """Добавляет базовые рекомендации по температуре"""
    if avg_temp < -20:
        recommendations['headwear'].extend(
            ['балаклава', 'шапка-ушанка с мехом', 'горнолыжная маска'])
        recommendations['upper_body'].extend(
            ['двойное термобелье', 'флисовая кофта', 'пуховый свитер',
             'арктический пуховик'])
        recommendations['lower_body'].extend(
            ['двойное термобелье', 'утепленные горнолыжные штаны',
             'зимние комбинезоны'])
        recommendations['footwear'].extend(
            ['арктические ботинки', 'валенки', 'снегоступы', 'термоноски'])
        recommendations['accessories'].extend(
            ['горнолыжные очки', 'согревающие стельки',
             'рукавицы с подогревом'])
        recommendations['important_tips'].append(
            '🥶 ЭКСТРЕМАЛЬНЫЙ МОРОЗ! Только специализированная арктическая одежда')

    elif -20 <= avg_temp < -10:
        recommendations['headwear'].extend(
            ['шапка-ушанка', 'горнолыжная маска', 'бафф'])
        recommendations['upper_body'].extend(
            ['термобелье', 'флисовая кофта', 'пуховка',
             'зимняя куртка с мехом'])
        recommendations['lower_body'].extend(
            ['термобелье', 'утепленные зимние штаны', 'сноубордические брюки'])
        recommendations['footwear'].extend(
            ['зимние ботинки с мехом', 'угги', 'термоноски'])
        recommendations['accessories'].extend(
            ['варежки', 'согревающие стельки', 'горнолыжные очки'])
        recommendations['important_tips'].append(
            '❄️ Сильный мороз! Обязательно термобелье и многослойность')

    elif -10 <= avg_temp < -5:
        recommendations['headwear'].extend(
            ['теплая вязаная шапка', 'шарф', 'балаклава'])
        recommendations['upper_body'].extend(
            ['термобелье', 'шерстяной свитер', 'пуховик', 'зимняя куртка'])
        recommendations['lower_body'].extend(
            ['термобелье', 'утепленные джинсы', 'зимние брюки'])
        recommendations['footwear'].extend(
            ['зимние ботинки', 'угги', 'теплые носки'])
        recommendations['accessories'].extend(['варежки', 'шерстяные носки'])
        recommendations['important_tips'].append(
            '🧊 Морозно! Не забудьте термобелье и теплую обувь')

    elif -5 <= avg_temp < 0:
        recommendations['headwear'].extend(['шапка', 'шарф', 'наушники'])
        recommendations['upper_body'].extend(
            ['флисовая кофта', 'толстовка', 'зимняя куртка', 'пуховик'])
        recommendations['lower_body'].extend(
            ['утепленные штаны', 'джинсы с термобельем', 'брюки на флисе'])
        recommendations['footwear'].extend(
            ['демисезонные ботинки', 'кроссовки на толстой подошве',
             'теплые носки'])
        recommendations['accessories'].append('перчатки')
        recommendations['important_tips'].append(
            '🌨️ Холодно! Теплая куртка и аксессуары обязательны')

    elif 0 <= avg_temp <= 5:
        recommendations['headwear'].extend(['шапка', 'шарф', 'бафф'])
        recommendations['upper_body'].extend(
            ['флисовая кофта', 'куртка', 'ветровка', 'толстовка с курткой'])
        recommendations['lower_body'].extend(
            ['джинсы', 'брюки', 'теплые штаны'])
        recommendations['footwear'].extend(
            ['кроссовки', 'ботинки', 'демисезонная обувь'])
        recommendations['accessories'].append('легкие перчатки')
        recommendations['important_tips'].append(
            '🌫️ Прохладно! Куртка и головной убор необходимы')

    elif 6 <= avg_temp <= 10:
        recommendations['headwear'].extend(['кепка', 'легкая шапка', 'бафф'])
        recommendations['upper_body'].extend(
            ['футболка с кофтой', 'рубашка с жилеткой', 'толстовка',
             'ветровка'])
        recommendations['lower_body'].extend(
            ['джинсы', 'брюки', 'легкие штаны'])
        recommendations['footwear'].extend(['кроссовки', 'мокасины', 'туфли'])
        recommendations['important_tips'].append(
            '🌤️ Свежо! Идеально для многослойной одежды')

    elif 10 < avg_temp <= 15:
        recommendations['headwear'].append('кепка или панама')
        recommendations['upper_body'].extend(
            ['футболка с легкой кофтой', 'рубашка', 'толстовка', 'ветровка'])
        recommendations['lower_body'].extend(['джинсы', 'брюки', 'чиносы'])
        recommendations['footwear'].extend(['кроссовки', 'кеды', 'лоферы'])
        recommendations['important_tips'].append(
            '😊 Комфортно! Легкая кофта может пригодиться')

    elif 15 < avg_temp <= 19:
        recommendations['headwear'].append('кепка или бейсболка')
        recommendations['upper_body'].extend(
            ['футболка', 'рубашка с длинным рукавом', 'легкая кофта'])
        recommendations['lower_body'].extend(
            ['джинсы', 'легкие брюки', 'бриджи'])
        recommendations['footwear'].extend(
            ['кроссовки', 'мокасины', 'эспадрильи'])
        recommendations['important_tips'].append(
            '🌞 Тепло! Идеальная погода для легкой одежды')

    elif 19 < avg_temp <= 24:
        recommendations['headwear'].append('панама или шляпа')
        recommendations['upper_body'].extend(
            ['футболка', 'майка', 'рубашка с коротким рукавом', 'топ'])
        recommendations['lower_body'].extend(
            ['шорты', 'легкие брюки', 'юбка', 'сарафан'])
        recommendations['footwear'].extend(
            ['сандалии', 'легкие кроссовки', 'босоножки'])
        recommendations['important_tips'].append(
            '☀️ Жарковато! Легкая и дышащая одежда')

    elif 24 < avg_temp <= 29:
        recommendations['headwear'].extend(
            ['панама', 'шляпа с широкими полями', 'бандана'])
        recommendations['upper_body'].extend(
            ['майка', 'футболка из хлопка', 'топ', 'саронг'])
        recommendations['lower_body'].extend(
            ['шорты', 'легкие юбки', 'льняные брюки', 'бермуды'])
        recommendations['footwear'].extend(
            ['сандалии', 'вьетнамки', 'открытая обувь'])
        recommendations['important_tips'].append(
            '🔥 Жарко! Только легкая и дышащая одежда')

    else:  # 30+ градусов
        recommendations['headwear'].extend(
            ['шляпа с полями', 'панама', 'кепка с сеткой'])
        recommendations['upper_body'].extend(
            ['майка', 'топ', 'боди', 'пляжная рубашка'])
        recommendations['lower_body'].extend(
            ['шорты', 'юбка', 'саронг', 'пляжные брюки'])
        recommendations['footwear'].extend(
            ['сандалии', 'вьетнамки', 'босоножки', 'пляжная обувь'])
        recommendations['important_tips'].append(
            '🌡️ ЭКСТРЕМАЛЬНАЯ ЖАРА! Минимум одежды, максимум защиты от солнца')


def _add_day_strategy_recommendations(recommendations: Dict[str, List],
                                      day_analysis: Dict):
    """Добавляет рекомендации по стратегии на день"""
    temp_diff = day_analysis['temp_difference']
    morning_temp = day_analysis['morning']['avg_temp']
    day_temp = day_analysis['day']['avg_temp']
    evening_temp = day_analysis['evening']['avg_temp']

    # Большой перепад температур
    if temp_diff > 10:
        recommendations['day_strategy'].append(
            '🎭 СИЛЬНЫЙ ПЕРЕПАД ТЕМПЕРАТУР! Многослойность обязательна')
        recommendations['upper_body'].extend(
            ['футболка', 'кофта/свитер', 'куртка/ветровка'])
        recommendations['accessories'].extend(['рюкзак', 'складной зонт'])
        recommendations['important_tips'].append(
            '🔄 Сильный перепад температур: утром - тепло одеться, днем - можно снять лишнее')

    elif temp_diff > 6:
        recommendations['day_strategy'].append(
            '🔄 Значительный перепад температур - одевайтесь слоями')
        recommendations['upper_body'].extend(
            ['футболка', 'кофта/толстовка', 'легкая куртка'])
        recommendations['important_tips'].append(
            '📊 Перепад температур значительный: планируйте одежду на весь день')

    # Утренняя прохлада + дневная жара
    if morning_temp < 15 and day_temp > 22:
        recommendations['day_strategy'].append(
            '🌅 Утром прохладно → ☀️ Днем жарко: берите с собой легкую одежду')
        recommendations['accessories'].append('легкая сумка для верхнего слоя')
        recommendations['important_tips'].append(
            '🌅→☀️ Утром куртка, днем - только футболка')

    # Вечерное похолодание
    if day_temp > 18 and evening_temp < 10:
        recommendations['day_strategy'].append(
            '🌇 Вечером сильно похолодает - возьмите теплую кофту')
        recommendations['upper_body'].append('теплый свитер/кофта на вечер')
        recommendations['important_tips'].append(
            '☀️→🌇 Днем тепло, вечером холодно - подготовьте теплый слой')

    # Постепенное потепление в течение дня
    if day_analysis.get('warming_trend'):
        recommendations['day_strategy'].append(
            '📈 Температура будет расти - удобная одежда для раздевания')
        recommendations['upper_body'].append(
            'одежда, которую легко снять/надеть')
        recommendations['important_tips'].append(
            '📈 Постепенное потепление: выбирайте модульную одежду')

    # Похолодание к вечеру
    if day_analysis.get('cooling_trend'):
        recommendations['day_strategy'].append(
            '📉 К вечеру похолодает - подготовьте теплый слой')
        recommendations['accessories'].append('термос с горячим напитком')
        recommendations['important_tips'].append(
            '📉 Похолодание к вечеру: возьмите дополнительный теплый слой')

    # Особые случаи
    if morning_temp < 5 and day_temp > 20:
        recommendations['day_strategy'].append(
            '❄️→🔥 Экстремальный перепад: утром зимняя одежда, днем - летняя')
        recommendations['important_tips'].append(
            '⚡ Экстремальный перепад: планируйте полную смену одежды')


def _add_weather_recommendations(recommendations: Dict[str, List],
                                 condition: str,
                                 chance_of_rain: int, wind_speed: float,
                                 uv_index: float):
    """Добавляет рекомендации по погодным условиям"""
    rain_keywords = ['дождь', 'ливень', 'гроза', 'мокрый', 'осадки', 'rain']
    is_rainy = any(keyword in condition.lower() for keyword in rain_keywords)

    # Рекомендации по осадкам
    if chance_of_rain > 20 or is_rainy:
        recommendations['accessories'].append('зонт')
        recommendations['important_tips'].append(
            '🌧️ Возможен дождь, возьмите зонт')

    if chance_of_rain > 50:
        recommendations['upper_body'].append(
            'дождевик или ветровка с влагозащитой')
        recommendations['footwear'] = ['резиновые сапоги',
                                       'водоотталкивающая обувь',
                                       'непромокаемые кроссовки']
        recommendations['important_tips'].append(
            '💧 Высокая вероятность дождя! Непромокаемая обувь обязательна')

    if chance_of_rain > 80:
        recommendations['upper_body'].append('водонепроницаемая куртка')
        recommendations['lower_body'].append('водоотталкивающие штаны')
        recommendations['important_tips'].append(
            '⛈️ Сильный дождь! Полная защита от воды рекомендуется')

    # Рекомендации по солнцу и УФ-индексу
    sunny_keywords = ['солнечно', 'ясно', 'sunny', 'clear']
    is_sunny = any(keyword in condition.lower() for keyword in sunny_keywords)

    if uv_index > 3 or is_sunny:
        recommendations['accessories'].append('солнцезащитные очки')
        recommendations['important_tips'].append('😎 Солнечно, защитите глаза')

    if uv_index > 6:
        recommendations['headwear'].extend(
            ['головной убор с козырьком', 'шляпа с полями'])
        recommendations['accessories'].append('солнцезащитный крем SPF 30+')
        recommendations['important_tips'].append(
            '⚠️ Высокий УФ-индекс! Обязательно используйте крем')

    if uv_index > 8:
        recommendations['upper_body'].append('одежда с УФ-защитой')
        recommendations['important_tips'].append(
            '☀️ Очень высокий УФ-индекс! Максимальная защита от солнца')

    # Рекомендации по ветру
    if wind_speed > 15:
        recommendations['upper_body'].append('ветровка')
        recommendations['accessories'].append('ветрозащитные очки')
        if wind_speed > 25:
            recommendations['headwear'].append('плотно сидящая шапка')
            recommendations['important_tips'].append(
                '💨 Сильный ветер! Одежда не должна развеваться')

    # Особые погодные условия
    if 'туман' in condition.lower():
        recommendations['accessories'].append('светоотражающие элементы')
        recommendations['important_tips'].append(
            '🌫️ Туманно! Используйте светоотражатели для безопасности')

    if 'гроза' in condition.lower():
        recommendations['important_tips'].append(
            '⚡ Гроза! Избегайте открытых пространств и металлических предметов')

#
# # Тестирование модуля
# if __name__ == "__main__":
#     # Тест базовых рекомендаций
#     test_recommendations = generate_clothing_recommendations(
#         avg_temp=15,
#         condition="Солнечно",
#         chance_of_rain=10,
#         wind_speed=5,
#         uv_index=4
#     )
#
#     print("✅ Тест базовых рекомендаций пройден!")
#     for category, items in test_recommendations.items():
#         print(f"{category}: {items}")
#
#     # Тест с анализом дня
#     day_analysis = {
#         'morning': {'avg_temp': 8, 'condition': 'Пасмурно'},
#         'day': {'avg_temp': 22, 'condition': 'Солнечно'},
#         'evening': {'avg_temp': 14, 'condition': 'Ясно'},
#         'temp_difference': 14,
#         'is_big_difference': True,
#         'warming_trend': True,
#         'cooling_trend': True
#     }
#
#     test_recommendations_with_day = generate_clothing_recommendations(
#         avg_temp=15,
#         condition="Солнечно",
#         chance_of_rain=10,
#         wind_speed=5,
#         uv_index=4,
#         day_analysis=day_analysis
#     )
#
#     print("\n✅ Тест с анализом дня пройден!")
#     print("Стратегия на день:", test_recommendations_with_day['day_strategy'])