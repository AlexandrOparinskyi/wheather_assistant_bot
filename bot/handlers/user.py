from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager

from bot.states import StartState, SettingsState
from bot.utils import (get_user_by_id,
                       create_user,
                       create_user_setting,
                       create_user_schedule)
from services import get_weather_recommendation_message

user_router = Router()


@user_router.message(CommandStart())
async def command_start(message: Message,
                        dialog_manager: DialogManager):
    user = await get_user_by_id(message.from_user.id)

    if user is None:
        await create_user(message.from_user.id,
                          message.from_user.first_name,
                          message.from_user.last_name,
                          message.from_user.username)
        await create_user_setting(message.from_user.id)
        await create_user_schedule(message.from_user.id)

        await dialog_manager.start(state=StartState.start)


@user_router.message(Command(commands="settings"))
async def command_settings(message: Message,
                           dialog_manager: DialogManager):
    user = await get_user_by_id(message.from_user.id)

    if user is None:
        return

    await dialog_manager.start(state=SettingsState.home)


@user_router.message(Command(commands="get_weather"))
async def get_weather(message: Message):
    user = await get_user_by_id(message.from_user.id)
    text = await get_weather_recommendation_message(user.user_settings.city)
    await message.answer(text)
