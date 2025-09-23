from aiogram.fsm.state import StatesGroup, State


class StartState(StatesGroup):
    start = State()
    info_setting = State()
    skip_setting = State()


class SettingsState(StatesGroup):
    home = State()
    notification_days_setting = State()
