from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

token = '6524110656:AAETBv1g6MnsgZKGzUj-yvsUMS_7j2aNqis'

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    greeting_message = "Hello! Welcome to the Food Ordering Bot. Click 'Order' to view the menu."
    
    # Create inline keyboard
    keyboard = InlineKeyboardMarkup()
    order_button = InlineKeyboardButton("Order", web_app=WebAppInfo(url = 'https://amirymax.github.io/2023-fall-lab-portfolio-amiri-z.-f./'))
    keyboard.add(order_button)

    # Send greeting message with inline keyboard
    await bot.send_message(user_id, greeting_message, reply_markup=keyboard)


# @dp.callback_query_handler(lambda c: c.data == 'order')
# async def order(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id

#     # Send the web app document to the user
#     await bot.send_message(user_id, "Click 'Open' to view the menu", reply_markup=InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton("Open", url=web_app_info.url)]
#         ]
#     ))

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)