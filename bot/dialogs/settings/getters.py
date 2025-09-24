from typing import Dict

from aiogram.types import User
from fluentogram import TranslatorHub

from bot.utils import get_weekdays_text, get_user_by_id


async def getter_setting_home(i18n: TranslatorHub,
                              event_from_user: User,
                              **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    weekdays = await get_weekdays_text(user)
    notification_days_setting = i18n.setting.notification.days.button()
    home_message = i18n.settings.home.text(
        username=user.first_name,
        current_city=user.user_settings.city,
        current_timezone=user.user_settings.timezone,
        weekdays=weekdays
    )

    return {"home_message": home_message,
            "notification_days_setting": notification_days_setting,
            "time_setting": i18n.setting.time.button(),
            "location_setting": i18n.setting.location.button()}


async def getter_notification_setting(i18n: TranslatorHub,
                                      event_from_user: User,
                                      **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    day_buttons = list(sorted(user.user_schedules,
                              key=lambda item: item.day_of_week.value))

    return {"setting_notification_text": i18n.settings.notification.text(),
            "buttons": day_buttons,
            "enable_weekdays_button": i18n.enable.weekdays.button(),
            "disable_weekdays_button": i18n.disable.weekdays.button(),
            "back_button": i18n.back.button()}


async def getter_location_setting(i18n: TranslatorHub,
                                  event_from_user: User,
                                  **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    setting_location_text = i18n.setting.location.text(
        current_city=user.user_settings.city
    )

    return {"setting_location_text": setting_location_text,
            "back_button": i18n.back.button()}
