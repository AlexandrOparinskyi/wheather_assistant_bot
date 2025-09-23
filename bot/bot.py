import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from bot.dialogs import register_dialogs
from bot.handlers import register_routers
from bot.middlewares import TranslatorRunnerMiddleware

logger = logging.getLogger(__name__)


async def main(
        token: str,
        hub: TranslatorHub,
        storage: RedisStorage | MemoryStorage = MemoryStorage()
) -> None:
    bot: Bot = Bot(token=token,
                   default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp: Dispatcher = Dispatcher(storage=storage)

    dp.update.middleware(TranslatorRunnerMiddleware())

    register_routers(dp)
    register_dialogs(dp)
    setup_dialogs(dp)

    try:
        await dp.start_polling(bot, _translator_hub=hub)
    except Exception as e:
        logger.error(f"Bot dont started: {e}")
