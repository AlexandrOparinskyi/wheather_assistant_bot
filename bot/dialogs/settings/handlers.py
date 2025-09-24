from time import timezone

from aiogram.client.session import aiohttp
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select, Button

from bot.states import SettingsState
from bot.utils import toggle_notification_status, enable_weekdays, \
    disable_weekdays, toggle_user_city


async def back_button_to_home(callback: CallbackQuery,
                              button: Button,
                              dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=SettingsState.home)


async def notification_days_setting(callback: CallbackQuery,
                                    button: Button,
                                    dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=SettingsState.notification_setting)


async def location_setting(callback: CallbackQuery,
                           button: Button,
                           dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=SettingsState.location_setting)


async def time_setting(callback: CallbackQuery,
                       button: Button,
                       dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=SettingsState.time_setting)


async def toggle_day_notification(callback: CallbackQuery,
                                  widget: Select,
                                  dialog_manager: DialogManager,
                                  item_id: str):
    await toggle_notification_status(callback.from_user.id,
                                     int(item_id))


async def enable_weekdays_button(callback: CallbackQuery,
                                 button: Button,
                                 dialog_manager: DialogManager):
    await enable_weekdays(callback.from_user.id)


async def disable_weekdays_button(callback: CallbackQuery,
                                  button: Button,
                                  dialog_manager: DialogManager):
    await disable_weekdays(callback.from_user.id)


async def send_location(message: Message,
                          widget: MessageInput,
                          dialog_manager: DialogManager):
    lat, lon = message.location.latitude, message.location.longitude
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        'lat': lat,
        'lon': lon,
        'format': 'json',
        'accept-language': 'ru',
        'zoom': 18
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()

    await toggle_user_city(message.from_user.id,
                           data.get("address").get("city"),
                           lon)

    await dialog_manager.switch_to(state=SettingsState.home)


async def error_send_location(message: Message,
                              widget: MessageInput,
                              dialog_manager: DialogManager):
    i18n = dialog_manager.middleware_data.get("i18n")
    dialog_manager.show_mode = ShowMode.NO_UPDATE
    await message.answer(
        text=i18n.invalid.location.message.text()
    )
