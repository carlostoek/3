from aiogram import types
from app.services.user_service import register_user, get_user_profile
from app.core.bot import dp

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await register_user(message.from_user.id, message.from_user.username, message.from_user.first_name)
    await message.answer("¡Bienvenido al bot narrativo!")

@dp.message_handler(commands=['perfil'])
async def profile_handler(message: types.Message):
    user_data = await get_user_profile(message.from_user.id)
    await message.answer(f"Nivel: {user_data['level']}\nPuntos: {user_data['points']}")