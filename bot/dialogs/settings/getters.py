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

    return {"home_message": i18n.settings.home.text(username=user.first_name,
                                                    weekdays=weekdays),
            "notification_days_setting": notification_days_setting,
            "time_setting": i18n.setting.time.button()}
