from aiogram_dialog import Dialog, Window

from bot.states import SettingsState

setting_dialog = Dialog(
    Window(
        state=SettingsState.home
    )
)