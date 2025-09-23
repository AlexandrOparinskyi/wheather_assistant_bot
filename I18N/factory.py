from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub

DIR_PATH = 'I18N/locales'


def create_translator_hub() -> TranslatorHub:
    return TranslatorHub(
        {'ru': ('ru', 'en'), 'en': 'en'},
        [
            FluentTranslator(
                locale='ru',
                translator=FluentBundle.from_files(
                    locale='ru',
                    filenames=[f'{DIR_PATH}/ru/LC_MESSAGES/settings.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/start.ftl']),
            ),
            FluentTranslator(
                locale='en',
                translator=FluentBundle.from_files(
                    locale='en',
                    filenames=[f'{DIR_PATH}/en/LC_MESSAGES/settings.ftl',
                               f'{DIR_PATH}/en/LC_MESSAGES/start.ftl']),
            ),
        ],
        root_locale='ru',
    )
