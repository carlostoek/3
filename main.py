from aiogram import executor
from app.core.bot import dp
import app.handlers.basic

if __name__ == '__main__':
    from app.core.database import engine, Base

    async def on_startup(dispatcher):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    executor.start_polling(dp, on_startup=on_startup)