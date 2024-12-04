# type_messages.py

from .config import BotEdit


# То что будет импортироваться при from type_messages import *
__all__ = ("types_message",)
type_messages = "Type_message"


# Проверка на тип сообщения
async def types_message(message):
    if message.text:
        first_char = message.text.strip()[0]  # Извлекаем первый символ текста (убираем лишние пробелы)
        if first_char in BotEdit.prefixs:
            message_types = "Команда"
        else:
            message_types = "Текст"
    elif message.photo:
        message_types = "Фото"
    elif message.sticker:
        message_types = "Стикер"
    elif message.animation:
        message_types = "Гиф"
    elif message.voice:
        message_types = "Видеосообщение"
    elif message.video_note:
        message_types = "Голосовое сообщение"
    elif message.video:
        message_types = "Видео"
    elif message.audio:
        message_types = "Аудио"
    elif message.document:
        message_types = "Документ"
    elif message.contact:
        message_types = "Контакт"
    elif message.location:
        message_types = "Локация"
    elif message.venue:
        message_types = "Venue"
    elif message.dice:
        message_types = "Бросок"
    elif message.story:
        message_types = "История"
    elif message.game:
        message_types = "Игра"
    elif message.new_chat_members:
        message_types = "Участник присоединился к нам!"
    elif message.left_chat_member:
        message_types = "Участник покинул чат..."
    elif message.boost_added:
        message_types = "Бууууст!"
    elif message.poll:
        message_types = "Опрос"
    else:
        message_types = "ОШИБКА! ОШИБКА!! ОШИБКА!!! НЕИЗВЕСТНЫЙ ТИП!!!!"
    return message_types
