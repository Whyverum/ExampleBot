# main.py
# Основной код проекта, который и соединяет в себе все его возможности

import asyncio
from aiogram import types
from aiogram.filters import Command
from BotSettings import *


# Обработчик команды /start
@dp.message(Command("start", "старт", "запуск", "пуск", "on", "вкл", "с", "s", "ы",
                    "ыефке", "cnfhn", "pfgecr", "gecr", prefix=prefixes, ignore_case=True))
async def command_start(message: types.Message):
    type_message = "Start"
    text = f"Привет, {message.from_user.full_name}! Я ваш бот."
    (logger.bind(custom_variable=type_message, user_var=f"@{message.from_user.username}")
     .info("Использовал(а) команду /start"))
    await message.reply(text=text)
    return text


# Обработчик команды /help
@dp.message(Command("help", "info", "помощь", "инфо", "?", "информация", "рудз", "штащ", "byaj",
                    "gjvjom", "byajhvfwbz", prefix=prefixes, ignore_case=True))
async def command_help(message: types.Message):
    type_message = "Help"
    text = f"Сообщение о помощи...."
    (logger.bind(custom_variable=type_message, user_var=f"@{message.from_user.username}")
     .info("Использовал(а) команду /help"))
    await message.reply(text=text)
    return text


# Обработчик всех иных сообщений
@dp.message()
async def all_message(message: types.Message):
    type_message = "Message"
    if message.text is not None:
        (logger.bind(custom_variable=type_message, user_var=f"@{message.from_user.username}")
         .info(f"Получено сообщение: {message.text}"))
        # Тут весь иной код для всех полученных сообщений
    else:
        type_msg = types_message(message)
        (logger.bind(custom_variable=type_msg, user_var=f"@{message.from_user.username}")
         .info(f"Получено сообщение: {type_msg}"))


# Запуск основного кода
async def main():
    setup_logger()  # Инициализация логгера
    await set_all()  # Установка первоначальной настройки
    await bot_get_info()    # Получение информации о боте

    # Вывод в консоль сообщения о старте бота
    (logger.bind(custom_variable="AEP", user_var="Console")
    .info(f"Начало запуска бота @{BotInfo.username}..."))

    start_info_out()  # Вывод в консоль информацию о боте
    await dp.start_polling(bot)  # Запуск опросника бота


# Вечная работа бота
if __name__ == "__main__":
    asyncio.run(main())
