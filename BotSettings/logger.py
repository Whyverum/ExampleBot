# BotSettings/logger.py
# Создание логгеров и подключение функций логирования в файлы

import sys
from loguru import logger
from .config import ImportantPath, max_size_log_file, logs_text, error_logs_text

# Настройка экспорта модулей
__all__ = ("logger", "setup_logger",)
type_messages = "Logger"


# Создание обычного логгера + логгер в файл
def setup_logger():
    logger.remove()  # Удаляем все логгеры

    # Пустой логгер для записи отступов в файл
    logger.add(ImportantPath.log_file,
               rotation=max_size_log_file,
               format="\n\n\n",
               backtrace=True,
               diagnose=True, )
    logger.remove()

    # Логгер для записи в файл с ротацией и диагностической информацией
    logger.add(ImportantPath.log_file,
               rotation=max_size_log_file,
               format=logs_text,
               backtrace=True,
               diagnose=True,
               level="INFO",
               filter=lambda record: record["level"].name == "INFO", )

    # Логгер для записи в файл ошибок
    logger.add(ImportantPath.log_error_file,
               rotation=max_size_log_file,
               format=logs_text,
               backtrace=True,
               diagnose=True,
               level="ERROR",
               filter=lambda record: record["level"].name == "ERROR", )

    # Логгер для вывода в консоль
    logger.add(sys.stderr,
               colorize=True,
               format=logs_text,
               level="INFO",
               filter=lambda record: record["level"].name == "INFO",)

    # Логгер для вывода в консоль только для уровня ERROR
    logger.add(sys.stderr,
               colorize=True,
               format=error_logs_text,
               level="ERROR",
               filter=lambda record: record["level"].name == "ERROR",)

    return f"Логгеры подключены!"
