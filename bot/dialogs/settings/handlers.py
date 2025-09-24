from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select, Button

from bot.states import SettingsState
from bot.utils import toggle_notification_status, enable_weekdays, disable_weekdays


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
