from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bosh_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📑Информация о грузе"),
            KeyboardButton(text="📋Мои заказы"),
        ],
        [
            KeyboardButton(text="📱Получить ID номер и адрес."),
            KeyboardButton(text="🇺🇿Наш адрес в Ташкенте"),
        ],
        [
            # KeyboardButton(text="🚚Ввод номера трека АВТО"),
            KeyboardButton(text="🚚Информация о треке"),
            KeyboardButton(text="☎Колл-центр"),
        ],
        [
            KeyboardButton(text="📦Грузы без номеров"),
            KeyboardButton(text="🌐Филиалы"),
        ],
    ], resize_keyboard=True
)

id_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔑Получить ID номер"),
            KeyboardButton(text="☎Колл-центр"),
        ],
    ], resize_keyboard=True
)

vil_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ташкент.Ш"),
            KeyboardButton(text="Ташкент"),
            KeyboardButton(text="Андижан")
        ],
        [
            KeyboardButton(text="Бухара"),
            KeyboardButton(text="Фергана"),
            KeyboardButton(text="Джиззаx")
        ],
        [
            KeyboardButton(text="Наманган"),
            KeyboardButton(text="Навои"),
            KeyboardButton(text="Кашкадарья")
        ],
        [
            KeyboardButton(text="Самарканд"),
            KeyboardButton(text="Сырдарья"),
            KeyboardButton(text="Сурхандарьинская"),
            KeyboardButton(text="Хорезм")
        ],
        [
            KeyboardButton(text="Главное меню")
        ],
    ]
)
only_boshmenu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Главное меню")
        ],
    ],
    resize_keyboard=True
)


only_boshmenu_ru_trek = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вернуться в главное меню")
        ],
    ],
    resize_keyboard=True
)

buyurtmalar_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Пришло на склад в Ташкенте"),
        ],
        [
            KeyboardButton(text="Поехал на китайский склад")
        ],
        [
            KeyboardButton(text="🏠Главное меню")
        ],
    ],
    resize_keyboard=True
)
