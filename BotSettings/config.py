# BotSettings/config.py
# Список практически всех переменных проекта

import os
from dotenv import load_dotenv


# Загружаем переменные из файла .env
load_dotenv()
bot_token = os.getenv("main_bot_token")
api_key = os.getenv("APIKey")
web_api_key = os.getenv("WebAPIKey")


# Шаблон логов для обычного логгера
logs_text = ("<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red> | </red> "
             "<blue>PRIMO-{extra[custom_variable]}</blue> <red> | </red> "
             "<red>{extra[user_var]}  | </red> <level>{message}</level>")

# Максимальный размер лог-файла
max_size_log_file = "500 MB"

# Шаблон логов для логгера-ошибок
error_logs_text = ("<red>{time:YYYY-MM-DD HH:mm:ss}  |  "
                   "ERROR-{extra[custom_variable]}  | "
                   "{extra[user_var]} | </red><level>{message}</level>")


# Класс с параметрами настройки бота
class BotEdit:
    name = "Имя бота"   # Описание имени бота
    description = "Привет, мое имя Бот! Рад с вами пообщаться!!!"  # Описание бота
    short_description = "Описание виджета бота"   # Описание виджета бота
    prefixs = ('$', '!', '.', '%', '&', ':', '|', '+', '-', '/', '~', '?')  # Доступные префиксы бота


# Создание словарей с id пользователей
class ListId:
    # Айди забанненых пользователей
    ban_list_ids = {
        6666666666666: "Лох",  # @username_ban1
    }

    # Айди администраторов бота
    adm_list_id = {
        1234567890: "Имя_админа",  # @username_admin
    }

    # Айди важных пользователей бота
    important_users_list_ids = {
        1234567890: "Имя_Админа",  # @username_admin
    }

    # Айди важных групп
    groups_list_id = {
        1087968824: "GroupAnonymousBot",
        -1000000000000: "Имя Чата",
    }

    # Айди важных каналов бота
    channel_list_id = {
        -1234567890: "Имя_канала",  # @username_admin
    }

    # Создание единого словаря важных ID
    important_ids = important_users_list_ids.copy()
    important_ids.update(adm_list_id)
    important_ids.update(groups_list_id)
    important_ids.update(channel_list_id)


# Класс с важными переменными-пути
class ImportantPath:
    # Пути к файлам логирования
    log_start = f"BotLogs/bot_start.log"
    log_file = f"BotLogs/bot.log"
    log_error_file = f"BotLogs/bot_error.log"
    log_info = f"BotLogs/bot_info.log"

    # Пути к хранению сообщений
    private_message = f"BotLogs/BotMessages/Личные"
    group_message = f"BotLogs/BotMessages/Группы"

    # Пути к хранению медиа
    bot_personal_media = f"BotSettings/MediaPersonal"
    bot_received_media = f"BotFiles/MediaReceived"
    user_avatar = f"BotFiles/UserAvatar"
    chat_avatar = f"BotFiles/ChatAvatar"
    channel_avatar = f"BotFiles/ChannelAvatar"

    # Названия директорий-хранилищ
    photo = "Photo"
    video = "Video"
    videonote = "VideoNote"
    gif = "GIF"
    document = "Document"
    voice = "Voice"
    youtube = "YouTube"

    # Названия директорий-хранилищ для закачки
    photo_directory = f"{bot_received_media}/{photo}/"
    video_directory = f"{bot_received_media}/{video}/"
    videonote_directory = f"{bot_received_media}/{videonote}/"
    gif_directory = f"{bot_received_media}/{gif}/"
    document_directory = f"{bot_received_media}/{document}/"
    voice_directory = f"{bot_received_media}/{voice}/"
    youtube_directory = f"{bot_received_media}/{youtube}/"
