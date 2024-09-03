from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📑Kargo haqida malumot"),
            KeyboardButton(text="📋Mening buyurtmalarim"),
        ],
        [
            KeyboardButton(text="📱Id raqam va Adress olish"),
            KeyboardButton(text="🇺🇿Toshkentdagi manzilimiz"),
        ],
        [
            # KeyboardButton(text="🚚Trek raqam kiritish AVTO"),
            KeyboardButton(text="🚚Trek haqida ma'lumot"),
            KeyboardButton(text="☎Call Center"),
        ],
        [
            KeyboardButton(text="📦Kodsiz yuklar"),
            KeyboardButton(text="🌐Filiallar"),
        ],
    ], resize_keyboard=True
)









id_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔑ID raqam olish"),
            KeyboardButton(text="☎Call Center"),
        ],
    ], resize_keyboard=True
)

vil_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent.sh"),
            KeyboardButton(text="Toshkent"),
            KeyboardButton(text="Andijon"),
        ],
        [
            KeyboardButton(text="Buxoro"),
            KeyboardButton(text="Farg'ona"),
            KeyboardButton(text="Jizzax"),

        ],
        [
            KeyboardButton(text="Namangan"),
            KeyboardButton(text="Navoiy"),
            KeyboardButton(text="Qashqadaryo"),
        ],
        [
            KeyboardButton(text="Samarqand"),
            KeyboardButton(text="Sirdaryo"),
            KeyboardButton(text="Surxandaryo"),
            KeyboardButton(text="Xorazm")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ],
    ]
)
only_boshmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bosh menu")
        ],
    ],
    resize_keyboard=True
)

only_boshmenu_trek = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bosh menuga qaytish")
        ],
    ],
    resize_keyboard=True
)

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/exel_xitoy"),
            KeyboardButton(text="/exel_toshkent")
        ],
        [
            KeyboardButton(text="/exel_xitoy"),
        ],
    ],
    resize_keyboard=True
)

buyurtmalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent omboriga kelgan"),
        ],
        [
            KeyboardButton(text="Xitoy omboriga borgan")
        ],
        [
            KeyboardButton(text="🏠Bosh menu")
        ],
    ],
    resize_keyboard=True
)