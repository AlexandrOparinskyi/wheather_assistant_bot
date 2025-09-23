from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format

from bot.states import SettingsState
from .getters import getter_setting_home

settings_dialog = Dialog(
    Window(
        Format("{home_message}"),
        Button(Format("{notification_days_setting}"),
               id="notification_days_setting",
               on_click=None),
        Button(Format("{time_setting}"),
               id="time_setting",
               on_click=None),
        getter=getter_setting_home,
        state=SettingsState.home
    )
)
