import asyncio
import logging

from fluentogram import TranslatorHub

from I18N import create_translator_hub
from config import load_config, Config
from bot import bot

logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
               '%(lineno)d - %(name)s - %(message)s'
    )
logger = logging.getLogger(__name__)


async def app() -> None:
    config: Config = load_config()

    translator_hub: TranslatorHub = create_translator_hub()

    await asyncio.gather(bot(
        token=config.tg_bot.token,
        hub=translator_hub,
    ))


if __name__ == '__main__':
    asyncio.run(app())