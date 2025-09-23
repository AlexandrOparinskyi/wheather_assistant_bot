import enum
from datetime import time

from sqlalchemy import ForeignKey, Enum, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Weekday(enum.Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    @property
    def display_name(self) -> str:
        names = {
            Weekday.MONDAY: "Понедельник",
            Weekday.TUESDAY: "Вторник",
            Weekday.WEDNESDAY: "Среда",
            Weekday.THURSDAY: "Четверг",
            Weekday.FRIDAY: "Пятница",
            Weekday.SATURDAY: "Суббота",
            Weekday.SUNDAY: "Воскресенье"
        }
        return names.get(self, "Ошибка ❌")

    @property
    def short_name(self) -> str:
        names = {
            Weekday.MONDAY: "Пн",
            Weekday.TUESDAY: "Вт",
            Weekday.WEDNESDAY: "Ср",
            Weekday.THURSDAY: "Чт",
            Weekday.FRIDAY: "Пт",
            Weekday.SATURDAY: "Сб",
            Weekday.SUNDAY: "Вс"
        }
        return names.get(self, "Ошибка ❌")

    @property
    def emoji(self) -> str:
        emojis = {
            Weekday.MONDAY: "😫",
            Weekday.TUESDAY: "🥱",
            Weekday.WEDNESDAY: "😔",
            Weekday.THURSDAY: "🥹",
            Weekday.FRIDAY: "🥳",
            Weekday.SATURDAY: "🤤",
            Weekday.SUNDAY: "😴"
        }
        return emojis.get(self, "📅")


class UserSchedule(Base):
    __tablename__ = 'user_schedules'

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id",
                                                    ondelete="CASCADE",))

    day_of_week: Mapped[Weekday] = mapped_column(Enum(Weekday))
    notification_time: Mapped[time] = mapped_column(Time,
                                                    default=time(8))
    is_enabled: Mapped[bool] = mapped_column(default=True)

    user = relationship("User", back_populates="user_schedules")

    @property
    def status_icon(self) -> str:
        return "✅" if self.is_enabled else "❌"
