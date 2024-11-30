# main.py (Установка aiogram, loguru - обязательная!)

import sys
import asyncio
from loguru import logger

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties


# Переменные с ключами API
TELEGRAM_BOT_TOKEN = '6501028155:AAEnBDnMtV1BsOqSFQVrU3pHK03TaFZ5g2c'
API_KEY = "void_key_api"

# Базовая настройка бота
dp = Dispatcher()
bot = Bot(token=TELEGRAM_BOT_TOKEN)
parse_mode = DefaultBotProperties(parse_mode=ParseMode.HTML)
prefixes = ('$', '!', '.', '%', '&', ':', '|', '+', '-', '/', '~', '?')


# Создание словарей с id пользователей
class ListId:
    admin_id = {}
    ban_list_id = {}
    important_group_id = {}


# Коды для редактирования текста
class TextEscape:
    RESET_ESCAPE = "\033[0m"  # Код для сброса форматирования
    BOLD_ESCAPE = "\033[1m"  # Код для включения жирного текста
    FAINT_ESCAPE = "\033[2m"  # Код для включения тонкого текста (редко поддерживается)
    KURTIV_ESCAPE = "\033[3m"  # Код для включения курсива
    UNDERLINE_ESCAPE = "\033[4m"  # Код для включения подчеркнутого текста
    BLINK_ESCAPE = "\033[5m"  # Код для включения мигающего текста (редко поддерживается)
    INVERT_ESCAPE = "\033[7m"  # Код для инверсированного цвета
    HIDDEN_ESCAPE = "\033[8m"  # Код для скрытого текста
    STRIKETHROUGH_ESCAPE = "\033[9m"  # Код для зачеркнутого текста

    # Коды для цвета текста
    BLACK_TEXT = "\033[30m"  # Черный текст
    RED_TEXT = "\033[31m"  # Красный текст
    GREEN_TEXT = "\033[32m"  # Зеленый текст
    YELLOW_TEXT = "\033[33m"  # Желтый текст
    BLUE_TEXT = "\033[34m"  # Синий текст
    MAGENTA_TEXT = "\033[35m"  # Пурпурный текст
    CYAN_TEXT = "\033[36m"  # Бирюзовый текст
    WHITE_TEXT = "\033[37m"  # Белый текст
    LIGHT_BLACK_TEXT = "\033[90m"  # Светлый черный (серый) текст
    LIGHT_RED_TEXT = "\033[91m"  # Светлый красный текст
    LIGHT_GREEN_TEXT = "\033[92m"  # Светлый зеленый текст
    LIGHT_YELLOW_TEXT = "\033[93m"  # Светлый желтый текст
    LIGHT_BLUE_TEXT = "\033[94m"  # Светлый синий текст
    LIGHT_MAGENTA_TEXT = "\033[95m"  # Светлый пурпурный текст
    LIGHT_CYAN_TEXT = "\033[96m"  # Светлый бирюзовый текст
    LIGHT_WHITE_TEXT = "\033[97m"  # Светлый белый текст

    # Коды для цвета фона
    BLACK_BACKGROUND = "\033[40m"  # Черный фон
    RED_BACKGROUND = "\033[41m"  # Красный фон
    GREEN_BACKGROUND = "\033[42m"  # Зеленый фон
    YELLOW_BACKGROUND = "\033[43m"  # Желтый фон
    BLUE_BACKGROUND = "\033[44m"  # Синий фон
    MAGENTA_BACKGROUND = "\033[45m"  # Пурпурный фон
    CYAN_BACKGROUND = "\033[46m"  # Бирюзовый фон
    WHITE_BACKGROUND = "\033[47m"  # Белый фон
    LIGHT_BLACK_BACKGROUND = "\033[100m"  # Светлый черный фон
    LIGHT_RED_BACKGROUND = "\033[101m"  # Светлый красный фон
    LIGHT_GREEN_BACKGROUND = "\033[102m"  # Светлый зеленый фон
    LIGHT_YELLOW_BACKGROUND = "\033[103m"  # Светлый желтый фон
    LIGHT_BLUE_BACKGROUND = "\033[104m"  # Светлый синий фон
    LIGHT_MAGENTA_BACKGROUND = "\033[105m"  # Светлый пурпурный фон
    LIGHT_CYAN_BACKGROUND = "\033[106m"  # Светлый бирюзовый фон
    LIGHT_WHITE_BACKGROUND = "\033[107m"  # Светлый белый фон


# Функция создания обычного логгера
async def logger_setup():
    logger.remove()
    logs = ("<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red> | </red> "
            "<blue>PRIMO-{extra[custom_variable]}</blue> <red> | </red>"
            " <red>{extra[user_var]}</red> <red> | </red><level>{message}</level>")
    logger.add(sys.stdout, colorize=True, format=logs, level="INFO")


# Функция создания логгера для ошибок
async def error_logger():
    logger.remove()
    error_logs = ("<red>{time:YYYY-MM-DD HH:mm:ss}  |  "
                  "ERROR-{extra[custom_variable]}  | "
                  " {extra[user_var]}  | </red><level>{message}</level>")
    logger.add(sys.stderr, colorize=True, format=error_logs, level="ERROR")


# Создаем команды в список бота
async def set_commands():
    bot_commands = [
        types.BotCommand(command="start", description="Запустить бота"),
        types.BotCommand(command="help", description="Получить помощь"),
        types.BotCommand(command="command", description="Пустая команда")
    ]
    await bot.set_my_commands(bot_commands)


# Обработчик команды /start
@dp.message(Command("start", "старт", "запуск", "пуск", "on", "вкл", "с", "s", "ы",
                    "ыефке", "cnfhn", "pfgecr", "gecr", prefix=prefixes, ignore_case=True))
async def command_start(message: types.Message):
    type_message = "Start"
    logger.bind(custom_variable=type_message, user_var=f"@{message.from_user.username}").info(
        "Использовал(а) команду /start")
    await message.reply(text=f"Привет, {message.from_user.full_name}! Я ваш бот.")


# Обработчик команды /help
@dp.message(Command("help", "info", "помощь", "инфо", "?", "информация", "рудз", "штащ", "byaj",
                    "gjvjom", "byajhvfwbz", prefix=prefixes, ignore_case=True))
async def command_help(message: types.Message):
    type_message = "Help"
    logger.bind(custom_variable=type_message, user_var=f"@{message.from_user.username}").info(
        "Использовал(а) команду /help")
    await message.reply(
        text="Сообщение о помощи...."
    )


# Обработчик всех иных сообщений
@dp.message()
async def all_message(message: types.Message):
    type_message = "Message"
    logger.bind(custom_variable=type_message, user_var=f"@{message.from_user.username}").info(
        f"Получено сообщение: {message.text}")
    # Тут весь иной код для всех полученных сообщений


# Запуск бота
async def main():
    await logger_setup()  # Инициализация логгера
    await set_commands()  # Установка команд
    bot_info = await bot.get_me()  # Получение информации о боте
    logger.bind(custom_variable="AEP", user_var="Console").info(f"Начало запуска бота @{bot_info.username}...")
    await dp.start_polling(bot)  # Запуск опросника бота


# Вечная работа бота
if __name__ == "__main__":
    asyncio.run(main())
