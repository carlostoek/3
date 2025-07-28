class Settings:
    BOT_TOKEN: str = "YOUR_BOT_TOKEN"
    DATABASE_URL: str = "sqlite+aiosqlite:///./bot_db.sqlite3"
    ADMIN_USER_IDS: list[int] = [123456789]
    VIP_CHANNEL_ID: int = -1001234567890
    FREE_CHANNEL_ID: int = -1001234567891