from typing import Dict, List, Tuple


def generate_clothing_recommendations(avg_temp: float, condition: str,
                                      chance_of_rain: int, wind_speed: float,
                                      uv_index: float,
                                      day_analysis: Dict = None) -> Dict[str, List]:
    """
    Генерирует практичные рекомендации по одежде с акцентом на утренние/вечерние условия
    """
    recommendations = {
        'headwear': [],
        'upper_body': [],
        'lower_body': [],
        'footwear': [],
        'accessories': [],
        'important_tips': [],
        'day_strategy': []
    }

    # Определяем ключевые температурные периоды
    morning_temp = day_analysis['morning']['avg_temp'] if day_analysis else avg_temp
    evening_temp = day_analysis['evening']['avg_temp'] if day_analysis else avg_temp
    day_temp = day_analysis['day']['avg_temp'] if day_analysis else avg_temp

    # Основная рекомендация строится на ХОЛОДНЕЙШЕМ периоде (утро/вечер)
    coldest_temp = min(morning_temp, evening_temp)

    # Базовые рекомендации по ХОЛОДНОМУ периоду
    _add_base_recommendations(recommendations, coldest_temp, morning_temp, day_temp)

    # Стратегия на день с учетом перепадов
    if day_analysis:
        _add_day_strategy_recommendations(recommendations, day_analysis, morning_temp, day_temp, evening_temp)

    # Погодные условия (ветер, дождь, УФ)
    _add_weather_recommendations(recommendations, condition, chance_of_rain, wind_speed, uv_index, morning_temp)

    # Убираем дубликаты
    for category in recommendations:
        recommendations[category] = list(dict.fromkeys(recommendations[category]))

    return recommendations


def _add_base_recommendations(recommendations: Dict[str, List], coldest_temp: float, morning_temp: float,
                              day_temp: float):
    """Добавляет базовые рекомендации по ХОЛОДНЕЙШЕМУ времени суток"""

    # Экстремальный холод
    if coldest_temp < -25:
        recommendations['headwear'].extend(['арктическая шапка-ушанка', 'балаклава'])
        recommendations['upper_body'].extend(['двойное термобелье', 'пуховой свитер', 'арктический пуховик'])
        recommendations['lower_body'].extend(['термобелье', 'утепленные горнолыжные штаны'])
        recommendations['footwear'].extend(['арктические ботинки', 'термоноски'])
        recommendations['important_tips'].append('🥶 ЭКСТРЕМАЛЬНЫЙ МОРОЗ! Только специализированная зимняя одежда')

    elif -25 <= coldest_temp < -15:
        recommendations['headwear'].extend(['шапка-ушанка', 'горнолыжная маска'])
        recommendations['upper_body'].extend(['термобелье', 'флисовая кофта', 'пуховик с мехом'])
        recommendations['lower_body'].extend(['термобелье', 'утепленные зимние штаны'])
        recommendations['footwear'].extend(['зимние ботинки с мехом', 'угги', 'термоноски'])
        recommendations['important_tips'].append('❄️ Сильный мороз! Обязательно термобелье и пуховик')

    elif -15 <= coldest_temp < -8:
        recommendations['headwear'].extend(['теплая вязаная шапка', 'шарф'])
        recommendations['upper_body'].extend(['термобелье', 'шерстяной свитер', 'зимняя куртка'])
        recommendations['lower_body'].extend(['термобелье', 'утепленные джинсы'])
        recommendations['footwear'].extend(['зимние ботинки', 'теплые носки'])
        recommendations['important_tips'].append('🧊 Морозно! Термобелье и зимняя куртка обязательны')

    elif -8 <= coldest_temp < -3:
        recommendations['headwear'].extend(['шапка', 'шарф'])
        recommendations['upper_body'].extend(['флисовая кофта', 'толстовка', 'зимняя куртка', 'пуховик'])
        recommendations['lower_body'].extend(['утепленные штаны', 'джинсы с термобельем'])
        recommendations['footwear'].extend(['демисезонные ботинки', 'теплые носки'])
        recommendations['important_tips'].append('🌨️ Холодно! Теплая куртка и шапка необходимы')

    elif -3 <= coldest_temp <= 2:
        recommendations['headwear'].extend(['шапка', 'шарф'])
        recommendations['upper_body'].extend(['флисовая кофта', 'куртка', 'ветровка', 'толстовка с курткой'])
        recommendations['lower_body'].extend(['джинсы', 'брюки'])
        recommendations['footwear'].extend(['кроссовки', 'ботинки'])
        recommendations['important_tips'].append('🌫️ Прохладно! Куртка и головной убор обязательны')

    elif 2 < coldest_temp <= 7:
        recommendations['headwear'].append('легкая шапка или кепка')
        recommendations['upper_body'].extend(['футболка с кофтой', 'рубашка с жилеткой', 'толстовка', 'ветровка'])
        recommendations['lower_body'].extend(['джинсы', 'брюки'])
        recommendations['footwear'].extend(['кроссовки', 'мокасины'])
        recommendations['important_tips'].append('🌤️ Свежо! Кофта или ветровка необходимы')

    elif 7 < coldest_temp <= 12:
        recommendations['headwear'].append('кепка')
        recommendations['upper_body'].extend(['футболка с легкой кофтой', 'рубашка', 'толстовка'])
        recommendations['lower_body'].extend(['джинсы', 'брюки', 'чиносы'])
        recommendations['footwear'].extend(['кроссовки', 'кеды'])
        recommendations['important_tips'].append('😊 Комфортно! Легкая кофта пригодится')

    elif 12 < coldest_temp <= 17:
        recommendations['upper_body'].extend(['футболка', 'рубашка с длинным рукавом', 'легкая кофта'])
        recommendations['lower_body'].extend(['джинсы', 'легкие брюки'])
        recommendations['footwear'].extend(['кроссовки', 'мокасины'])
        recommendations['important_tips'].append('🌞 Тепло! Идеальная погода для легкой одежды')

    elif 17 < coldest_temp <= 22:
        recommendations['upper_body'].extend(['футболка', 'майка', 'рубашка с коротким рукавом'])
        recommendations['lower_body'].extend(['шорты', 'легкие брюки', 'юбка'])
        recommendations['footwear'].extend(['сандалии', 'легкие кроссовки'])
        recommendations['important_tips'].append('☀️ Жарковато! Легкая одежда')

    elif 22 < coldest_temp <= 27:
        recommendations['headwear'].append('панама или кепка')
        recommendations['upper_body'].extend(['майка', 'футболка из хлопка', 'топ'])
        recommendations['lower_body'].extend(['шорты', 'легкие юбки', 'льняные брюки'])
        recommendations['footwear'].extend(['сандалии', 'вьетнамки'])
        recommendations['important_tips'].append('🔥 Жарко! Легкая и дышащая одежда')

    else:  # 28+ градусов
        recommendations['headwear'].extend(['шляпа с полями', 'панама'])
        recommendations['upper_body'].extend(['майка', 'топ', 'пляжная рубашка'])
        recommendations['lower_body'].extend(['шорты', 'юбка', 'саронг'])
        recommendations['footwear'].extend(['сандалии', 'вьетнамки', 'босоножки'])
        recommendations['important_tips'].append('🌡️ ЭКСТРЕМАЛЬНАЯ ЖАРА! Минимум одежды, защита от солнца')


def _add_day_strategy_recommendations(recommendations: Dict[str, List],
                                      day_analysis: Dict,
                                      morning_temp: float,
                                      day_temp: float,
                                      evening_temp: float):
    """Добавляет практичные рекомендации по стратегии на день"""
    temp_diff = day_temp - morning_temp
    evening_diff = day_temp - evening_temp

    # Большой перепад температур: утром холодно, днем тепло
    if temp_diff > 12:
        recommendations['day_strategy'].append(
            '🌅❄️→☀️🔥 Утром очень холодно, днем жарко - наденьте куртку, которую можно снять')
        recommendations['important_tips'].append('🎒 Возьмите с собой сумку или рюкзак для куртки')

    elif temp_diff > 8:
        recommendations['day_strategy'].append('🌅🧊→☀️🌡️ Утром холодно, днем тепло - куртка понадобится только утром')
        recommendations['important_tips'].append('🕶️ Днем будет тепло - можно снять верхнюю одежду')

    elif temp_diff > 5:
        recommendations['day_strategy'].append('🌅🌫️→☀️😊 Утром прохладно, днем комфортно - легкая куртка пригодится')

    # Вечернее похолодание
    if evening_diff > 8:
        recommendations['day_strategy'].append('🌇❄️ Вечером сильно похолодает - подготовьте теплую одежду')
        recommendations['upper_body'].append('теплый свитер или кофта на вечер')

    elif evening_diff > 5:
        recommendations['day_strategy'].append('🌇🌫️ Вечером станет прохладнее - возьмите кофту')

    # Утренние осадки
    morning_rain = day_analysis.get('morning', {}).get('chance_of_rain', 0)
    if morning_rain > 60:
        recommendations['day_strategy'].append('🌧️☔ Утром сильный дождь - непромокаемая одежда обязательна')
    elif morning_rain > 30:
        recommendations['day_strategy'].append('🌧️ Утром возможен дождь - возьмите зонт')

    # Утренний ветер
    morning_wind = day_analysis.get('morning', {}).get('wind_speed', 0)
    if morning_wind > 15:
        recommendations['day_strategy'].append('💨🌬️ Утром сильный ветер - ветровка обязательна')
    elif morning_wind > 8:
        recommendations['day_strategy'].append('💨 Утром ветрено - нужна ветровка')


def _add_weather_recommendations(recommendations: Dict[str, List],
                                 condition: str,
                                 chance_of_rain: int,
                                 wind_speed: float,
                                 uv_index: float,
                                 morning_temp: float):
    """Добавляет рекомендации по погодным условиям с акцентом на утро"""
    rain_keywords = ['дождь', 'ливень', 'гроза', 'мокрый', 'осадки']
    is_rainy = any(keyword in condition.lower() for keyword in rain_keywords)

    # Рекомендации по осадкам
    if chance_of_rain > 70:
        recommendations['upper_body'].append('водонепроницаемая куртка')
        recommendations['footwear'] = ['резиновые сапоги', 'непромокаемые ботинки']
        recommendations['accessories'].append('зонт')
        recommendations['important_tips'].append('⛈️ Сильный дождь! Водонепроницаемая одежда обязательна')

    elif chance_of_rain > 40:
        recommendations['upper_body'].append('дождевик или куртка с влагозащитой')
        recommendations['footwear'].append('непромокаемая обувь')
        recommendations['accessories'].append('зонт')
        recommendations['important_tips'].append('🌧️ Дождь! Возьмите зонт и непромокаемую обувь')

    elif chance_of_rain > 20 or is_rainy:
        recommendations['accessories'].append('зонт')
        recommendations['important_tips'].append('☔ Возможен дождь - зонт пригодится')

    # Рекомендации по ветру
    if wind_speed > 20:
        recommendations['upper_body'].append('ветровка')
        recommendations['headwear'].append('плотно сидящая шапка')
        recommendations['important_tips'].append('💨 Сильный ветер! Ветровка и надежная шапка обязательны')

    elif wind_speed > 12:
        recommendations['upper_body'].append('ветровка')
        recommendations['important_tips'].append('💨 Ветрено! Ветровка будет кстати')

    elif wind_speed > 8:
        recommendations['upper_body'].append('ветровка')

    # Рекомендации по УФ-индексу
    if uv_index > 8:
        recommendations['headwear'].append('головной убор с козырьком')
        recommendations['accessories'].extend(['солнцезащитные очки', 'солнцезащитный крем SPF 50+'])
        recommendations['important_tips'].append('☀️ Очень высокий УФ-индекс! Обязательны крем и головной убор')

    elif uv_index > 6:
        recommendations['headwear'].append('кепка или панама')
        recommendations['accessories'].extend(['солнцезащитные очки', 'солнцезащитный крем SPF 30+'])
        recommendations['important_tips'].append('🔆 Высокий УФ-индекс! Защита от солнца обязательна')

    elif uv_index > 3:
        recommendations['accessories'].append('солнцезащитные очки')
        recommendations['important_tips'].append('😎 Солнечно - защитите глаза')
