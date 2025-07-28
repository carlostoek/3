from app.models.user import User
from app.core.database import SessionLocal
from sqlalchemy.future import select

async def register_user(user_id: int, username: str, first_name: str):
    async with SessionLocal() as session:
        result = await session.execute(select(User).where(User.user_id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            new_user = User(user_id=user_id, username=username, first_name=first_name)
            session.add(new_user)
            await session.commit()

async def get_user_profile(user_id: int) -> dict:
    async with SessionLocal() as session:
        result = await session.execute(select(User).where(User.user_id == user_id))
        user = result.scalar_one()
        return {"level": user.level, "points": user.points}