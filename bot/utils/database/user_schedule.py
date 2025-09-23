from sqlalchemy import insert

from database import get_async_session, UserSchedule, Weekday


async def create_user_schedule(user_id: int) -> None:
    created_values = [
        {"user_id": user_id,
         "day_of_week": day}
        for day in Weekday
    ]

    async with get_async_session() as session:
        await session.execute(insert(UserSchedule), created_values)
        await session.commit()
