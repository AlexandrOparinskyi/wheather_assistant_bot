from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select, Row
from aiogram_dialog.widgets.text import Format

from bot.states import SettingsState
from .getters import (getter_setting_home,
                      getter_notification_setting,
                      getter_location_setting)
from .handlers import (notification_days_setting,
                       toggle_day_notification,
                       enable_weekdays_button,
                       disable_weekdays_button,
                       back_button_to_home,
                       time_setting,
                       location_setting,
                       send_location,
                       error_send_location)

settings_dialog = Dialog(
    Window(
        Format("{home_message}"),
        Button(Format("{notification_days_setting}"),
               id="notification_days_setting",
               on_click=notification_days_setting),
        Button(Format("{time_setting}"),
               id="time_setting",
               on_click=time_setting),
        Button(Format("{location_setting}"),
               id="location_setting",
               on_click=location_setting),
        getter=getter_setting_home,
        state=SettingsState.home
    ),
    Window(
        Format("{setting_notification_text}"),
        Group(Select(id="days_toggle",
                     item_id_getter=lambda x: x.day_of_week.value,
                     items="buttons",
                     text=Format("{item.status_icon} "
                                 "{item.day_of_week.short_name}"),
                     on_click=toggle_day_notification),
              width=4),
        Row(Button(Format("{enable_weekdays_button}"),
                   id="enable_weekdays_button",
                   on_click=enable_weekdays_button),
            Button(Format("{disable_weekdays_button}"),
                   id="disable_weekdays_button",
                   on_click=disable_weekdays_button)),
        Button(Format("{back_button}"),
               id="back_button",
               on_click=back_button_to_home),
        getter=getter_notification_setting,
        state=SettingsState.notification_setting
    ),
    Window(
        Format("{setting_location_text}"),
        MessageInput(func=send_location,
                     content_types=ContentType.LOCATION),
        MessageInput(func=error_send_location,
                     content_types=ContentType.ANY),
        Button(Format("{back_button}"),
               id="back_button",
               on_click=back_button_to_home),
        getter=getter_location_setting,
        state=SettingsState.location_setting
    )
)
