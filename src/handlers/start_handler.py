from aiogram.types import Message

async def start_handler(message: Message):
    """
    Manejador para el comando /start. Responde con un saludo.
    """
    await message.answer("¡Hola! Bienvenido al bot de Telegram.")