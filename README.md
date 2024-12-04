## PRIMO_aiogram_bot


---
## Приветствие

Здравствуй, <u>**дорогой пользователь**</u>! 
Меня зовут *Лейн*, я думаю, мы вряд ли с тобой знакомы, 
но это и не важно.

Этот проект, нужен для того, чтобы каждый мог 
создать своего простенького *бота* на основе **Aiogram**. 
Этот **шаблон** позволит вам получить все возможные функции от создания *клавиатур*, 
до создания *логгеров* или *машины состояний*.


---
## Навигация:

-  ### [Приветствие](#Приветствие)
- ### [Первый запуск бота](#Запуск)
- ### [Его возможности](#Возможности)
- ### [Прочее](#Прочее)
- ### [Наполнение](#Наполнение)
- ### [Прощание](#Прощание)


---
## Запуск

Так что, давайте поговорим не много о самом проекте. 
Для начала проект, что вы получили с **GitHub**, имеет небольшую особенность 
для Windows-пользователей, а именно файл **project.bat**. 
Активировав этот файл через *консоль* с помощью команды: 
**start project**.
Вы сможете установить локальное окружение, обновить библиотеки и запустить бота. Вам
не понадобится думать и настраивать бота, все что вам необходимо это иметь 
установленным **Python 3.13** и **GIT**. Так он автоматически, он создаст:

- локальное окружение
- установит все необходимые библиотеки
- создаст локальный **GIT** репозиторий
- и запустит сам **main.py** (*основной файл бота*)


---
## Возможности

Поэтому вы уже получите возможность пользоваться системой **GIT**. Также из плюсов можно
выделить многое другое например:
- Работа с репозиториями и системой GIT
- Удобное логирование с помощью loguru
- Базовый функционал бота
- И многое другое!


---
## Наполнение
Основными файлами этого шаблона являются:

- **project.bat**   &nbsp; [*Файл bat, что создаст локальное окружение и подгрузит библиотеки*]
  - **poetry.lock**   &nbsp; [*Файл poetry, в котором находятся ссылки на библиотеки*]
  - **pypproject.toml**   &nbsp; [*Файл poetry, в котором хранятся все библиотеки*]


- **main.py** &nbsp; [*Является стартовым файлом всего проекта*]


- **settings**  &nbsp; [*Директория библиотека со всеми нужными функциями*]
  - **__ init __.py**   &nbsp; [*Инициализация пакета **settings***]
  - **bots.py**     &nbsp; [*Инициализация бота и получение информации о нем*]
  - **config.py**   &nbsp; [*Файл конфиг, в котором находятся листы с **настройками** и **id***]
  - **bot_logger.py**   &nbsp; [*Создает логгеры от loguru, для ошибок и информации*]
  - **decorator.py**   &nbsp; [*Библиотека-декоратор консоли, меняет цвета и стили текста*]
  - **types_message.py**   &nbsp; [*Функция, что способна определить тип сообщения*]


- **.gitignore**    &nbsp; [*Файл, который не даст скопировать в репозиторий определенный контент*]


- **.env**    &nbsp; [*Файл локального окружения, в котором хранится токен бота*]


- **README.md**   &nbsp; [*Файл с документацией к проекту*]


---
## Прощание

Я очень рад, что вы пользуетесь этим проектом, и надеюсь, 
что я буду улучшать его все дальше и дальше. Удачи, вам и конечно же...

***Вперед за Истиной, Дорогой Друг!*** 

-&nbsp;**Verum.**
=======
Привет, это шаблон для базовых ботов нф aiogram  с реализацией всего необходимого
#   S h a b l o n B o t  
 #   S h a b l o n P a r t B o t  
 