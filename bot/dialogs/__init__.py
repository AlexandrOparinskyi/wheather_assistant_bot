from aiogram import Router

from .start import register_start_dialogs


def register_dialogs(router: Router):
    register_start_dialogs(router)
