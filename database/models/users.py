from datetime import datetime
from typing import Optional

from sqlalchemy import func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[Optional[str]] = mapped_column(nullable=True)
    first_name: Mapped[str]
    last_name: Mapped[Optional[str]] = mapped_column(nullable=True)
    is_banned: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 default=func.now())
