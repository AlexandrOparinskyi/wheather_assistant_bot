from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select


async def toggle_day_notification(callback: CallbackQuery,
                                  widget: Select,
                                  dialog_manager: DialogManager,
                                  item_id: str):
    pass