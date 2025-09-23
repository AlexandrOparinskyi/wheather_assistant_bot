from typing import Optional

from sqlalchemy import insert, select

from database import get_async_session, UserSetting


async def get_user_setting_by_id(user_id: int) -> Optional[UserSetting]:
    async with get_async_session() as session:
        return await session.scalar(select(UserSetting).where(
            UserSetting.user_id == user_id
        ))


async def create_user_setting(user_id: int) -> None:
    async with get_async_session() as session:
        await session.execute(insert(UserSetting).values(
            user_id=user_id
        ))
        await session.commit()
