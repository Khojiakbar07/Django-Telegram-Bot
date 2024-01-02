import logging
from aiogram import Bot, Dispatcher, executor, types
from api import create_user, create_feedback
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from states import FeedbackState

API_TOKEN = '6734016800:AAGFEnYOlvVr0rMTEPYBQLMVTb9V6f1BGoQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token='6734016800:AAGFEnYOlvVr0rMTEPYBQLMVTb9V6f1BGoQ')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu Aleykum\nDjango-Aiogram botimizga xush kelibsiz!", reply_markup=button)
    print(create_user(message.from_user.username, message.from_user.first_name, message.from_user.id))

@dp.message_handler(Text(startswith="Talab va Takliflar"))
async def feedback_1(message: types.Message):
    await message.answer("Xabar matnini yuboring.")
    await FeedbackState.body.set()
    
@dp.message_handler(state = FeedbackState.body)
async def feedback_2(message: types.Message, state:FSMContext):
    await message.answer(create_feedback(message.from_user.id,  message.text))
    await state.finish()


    executor.start_polling(dp, skip_updates=False)
