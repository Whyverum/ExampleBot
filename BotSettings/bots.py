# BotSettings/bots.py
# Создание и настройка бота в одном файле

from datetime import datetime
from .config import BotEdit, bot_token
from aiogram import Dispatcher, Bot, types, F
from aiogram.types import ChatAdministratorRights
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# Настройка экспорта модулей
__all__ = ("bot", "dp", "F_Media", "prefixes", "BotInfo", "set_all", "bot_get_info")


# Базовая настройка и объявление бота
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("\n%Y-%m-%d %H:%M:%S")
dp["is_active"] = True  # Флаг активности бота
bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

F_Media = F.photo | F.document | F.video | F.animation | F.voice | F.video_note  # Фильтр-медиа
prefixes = ('$', '!', '.', '%', '&', ':', '|', '+', '-', '/', '~', '?')     # Создание префиксов бота


# Класс для хранения данных о боте
class BotInfo:
    # Статические переменные для хранения данных
    id = None
    first_name = None
    last_name = None
    username = None
    can_join_groups = None
    can_read_all_group_messages = None
    language_code = "Python-Aiogram"
    is_premium = None
    added_to_attachment_menu = None
    supports_inline_queries = None
    can_connect_to_business = None
    has_main_web_app = None

    # Метод для обновления данных
    @classmethod
    def update(cls, bot_info):
        cls.id = bot_info.id
        cls.first_name = bot_info.first_name
        cls.last_name = bot_info.last_name
        cls.username = bot_info.username
        cls.can_join_groups = bot_info.can_join_groups
        cls.can_read_all_group_messages = bot_info.can_read_all_group_messages
        cls.is_premium = bot_info.is_premium
        cls.added_to_attachment_menu = bot_info.added_to_attachment_menu
        cls.supports_inline_queries = bot_info.supports_inline_queries
        cls.can_connect_to_business = bot_info.can_connect_to_business
        cls.has_main_web_app = bot_info.has_main_web_app


# Функция получения данных о боте
async def bot_get_info():
    bot_info_data = await bot.get_me()

    # Обновляем данные о боте в BotInfo
    BotInfo.update(bot_info_data)

    # Возвращаем обновленные данные
    return {
        'bot_info': bot_info_data,
        'id': bot_info_data.id,
        'first_name': bot_info_data.first_name,
        'last_name': bot_info_data.last_name,
        'username': bot_info_data.username,
        'can_join_groups': bot_info_data.can_join_groups,
        'can_read_all_group_messages': bot_info_data.can_read_all_group_messages,
        'language_code': "Python-Aiogram",
        'is_premium': bot_info_data.is_premium,
        'added_to_attachment_menu': bot_info_data.added_to_attachment_menu,
        'supports_inline_queries': bot_info_data.supports_inline_queries,
        'can_connect_to_business': bot_info_data.can_connect_to_business,
        'has_main_web_app': bot_info_data.has_main_web_app,
    }


# Функция для выполнения всех настроек, если они не совпадают
async def set_all():
    await set_adm_rights()
    await set_bot_name()
    await set_bot_description()
    await set_bot_short_description()
    return f"Автономная настройка бота - завершена!"


# Функция установки имени бота
async def set_bot_name():
    # Получаем текущее имя бота
    current_name = (await bot.get_me()).first_name

    # Проверяем, совпадает ли текущее имя с тем, которое мы хотим установить
    if current_name != BotEdit.name:
        await bot.set_my_name(BotEdit.name)
        return f"Имя бота изменено на {BotEdit.name}!"
    else:
        return f"Имя бота уже установлено как {current_name}. Изменений не требуется."


# Функция установки прав администратора
async def set_adm_rights():
    # Применить права администратора для бота
    rights = ChatAdministratorRights(
        is_anonymous=False,
        can_manage_chat=True,
        can_delete_messages=True,
        can_manage_video_chats=True,
        can_restrict_members=True,
        can_promote_members=True,
        can_change_info=True,
        can_invite_users=True,
        can_post_stories=True,
        can_edit_stories=True,
        can_delete_stories=True,
        can_post_messages=True,
        can_edit_messages=True,
        can_pin_messages=True,
        can_manage_topics=True,
    )

    # Применяем права только в случае изменения
    current_rights = await bot.get_my_default_administrator_rights()
    if current_rights != rights:
        await bot.set_my_default_administrator_rights(rights)
        return f"Админ права бота изменены!"
    else:
        return "Админ права уже установлены и не требуют изменений."


# Функция установки описания бота
async def set_bot_description():
    # Получаем текущее описание бота
    current_description = await bot.get_my_description()

    # Проверяем, совпадает ли текущее описание с тем, которое мы хотим установить
    if current_description != BotEdit.description:
        await bot.set_my_description(description=BotEdit.description)
        return f"Описание бота изменено!"
    else:
        return "Описание бота уже установлено и не требует изменений."


# Функция установки короткого описания бота
async def set_bot_short_description():
    # Получаем текущее короткое описание бота
    current_short_description = await bot.get_my_short_description()

    # Проверяем, совпадает ли текущее короткое описание с тем, которое мы хотим установить
    if current_short_description != BotEdit.short_description:
        await bot.set_my_short_description(short_description=BotEdit.short_description)
        return f"Короткое описание бота изменено!"
    else:
        return f"Короткое описание бота уже установлено и не требует изменений."


# Создаем команды в список бота
async def set_commands():
    bot_commands = [
        types.BotCommand(command="start", description="Запустить бота"),
        types.BotCommand(command="help", description="Получить помощь"),
        types.BotCommand(command="command", description="Пустая команда"),
    ]
    await bot.set_my_commands(bot_commands)
