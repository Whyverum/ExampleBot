# bot_logger.py

import sys
from loguru import logger

# Все то что импортируется при: from bot_logger import *
__all__ = ("sys", "logger", "setup_logger", )


# Функция создания логгеров-loguru
async def setup_logger():
    logger.remove()  # Удаляем все логгеры

    # Шаблон логов для обычного логгера
    logs_text = ("<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red> | </red> "
                 "<blue>PRIMO-{extra[custom_variable]}</blue> <red> | </red> "
                 "<red>{extra[user_var]}  | </red> <level>{message}</level>")

    # Шаблон логов для логгера-ошибок
    error_logs_text = ("<red>{time:YYYY-MM-DD HH:mm:ss}  |  "
                       "ERROR-{extra[custom_variable]}  | "
                       "{extra[user_var]} | </red><level>{message}</level>")

    # Логгер для записи в файл с ротацией и диагностической информацией
    logger.add("bot.log",
               rotation="500 MB",
               backtrace=True,
               diagnose=True)

    # Логгер для вывода в консоль
    logger.add(sys.stderr,
               colorize=True,
               format=logs_text,
               level="INFO",
               filter=lambda record: record["level"].name == "INFO", )

    # Логгер для вывода в консоль только для уровня ERROR
    logger.add(sys.stderr,
               colorize=True,
               format=error_logs_text,
               level="ERROR",
               filter=lambda record: record["level"].name == "ERROR", )

    return f"Логгеры подключены!"