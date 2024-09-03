from aiogram import types

from keyboards.default.bosh_menu_ru import bosh_menu_ru
from loader import dp, bot
from utils.db_api.users_sql import Database_User

db_user = Database_User()


@dp.message_handler(text="🏠Главное меню")
async def bosh_menushu(message: types.Message):
    await message.answer(f"📲Выберите нужный раздел", reply_markup=bosh_menu_ru)

@dp.message_handler(text="📑Информация о грузе")
async def kargo_about(message: types.Message):
    await message.answer(f"ИНФОРМАЦИЯ О ГРУЗЕ\n"
    f"🚚АВТОГРУЗ - 7$ за 1 кг груза, срок прибытия 15-20 дней со дня поступления на китайский склад.\n"
    f"Нет минимума\n"
    f"Есть манометр\n"
    f"✈️ АВИА ГРУЗ - 11,5$ за 1 кг груза. 7-10 дней со дня упаковки\n"
    f"Существует минимум\n"
    f"Есть манометр\n"
    f"‼️Список товаров, которые нельзя ввозить из Китая ‼️\n"
    f"❌Наркотики, психотропные вещества (сигареты, кальянный табак).\n"
    f"❌2) Алкогольная продукция.\n"
    f"❌3) Взрыв опасных веществ (фейерверки, салюты, петарды), а также химических веществ\n"
    f"❌4) Провокационный экстремизм, насилие, порнография, видеоматериалы, оказывающие негативное влияние на общество, книги, публикации, материалы.\n"
    f"❌5)Медицинское оборудование и инструменты, медикаменты, лекарственные препараты (травы, мази, витамины, бальзамы, препараты).\n"
    f"❌6) Косметологическое оборудование (татуаж, игла, шприц).\n"
    f"❌7) Лазерные указки (увеличение лазерных лучей).\n"
    f"❌8) Дроны (самолеты).\n"
    f"❌9) Игровые автоматы (покерные фишки).\n"
    f"❌10) Мобильные телефоны (запчасти кроме экрана, планшета с сим-картой).\n"
    f"❌11) Драгоценные металлы (золото, серебро...)\n"
    f"❌12) Счетчики электроэнергии, газа, воды\n"
    f"❌13) Автомобильные двигатели.\n"
    f"❌14) Огнестрельное оружие, электрошокеры, пневматическое и газовое оружие, патроны для стрельбы (патроны, луки и стрелы).\n"
    f"❌15) Интимные игрушки, куклы (стимуляторы, мази).\n"
    f"❌16) этикетки на продукты питания без реквизитов.\n"
    f"❌17) Продукты питания с одобрения руководства.\n\n"
    f"✈️Авиада вместе с вышеперечисленным товаром ❌️❌️❌\n"
    f"Товары на батарейках 🔋🪫\n"
    f"Вещи с магнитами ⚙️\n"
    f"Любые жидкости 💦\n"
    f"Линзы 👁\n"
    f"Клей 💥\n"
    f"Порошок, порошкообразные вещи НЕВОЗМОЖНО ❌\n\n"
    f"🚫 Пожалуйста, не подбрасывайте такие грузы в воздух ‼")
    await message.answer(f"Следите за главными новостями в нашей группе\n"
                         f"👉https://t.me/barakatezkor_cargo\n\n"
                         f"Следите за нашей обучающей группой\n"
                         f"👉https://t.me/barakakargo_darslik")


@dp.message_handler(text="☎Колл-центр")
async def call_centeruchun(message: types.Message):
    photo = open("./data/RASM/call_center.jpg", "rb")
    await message.answer_photo(photo=photo)


@dp.message_handler(text="📱Получить ID номер и адрес.")
async def id_adress_olish(message: types.Message):
    try:
        await db_user.create()
    except:
        pas = 1
    user = await db_user.select_user(user_id=str(message.from_user.id))
    btk = user[2]
    video = open("./data/video.mp4", "rb")
    await bot.send_video(message.chat.id, video=video)
    await message.answer(f"Вам присвоен номер   БТК-{btk}  ")
    await message.answer(f"Адрес нашего склада в Китае:")
    await message.answer(f"联系电话：15267397101\n浙江省，金华市，义乌市，稠城街道，兴港小区152幢二单元一楼门面")
    await message.answer(f"Спасибо за сотрудничество с нами\n"
                         f"Удачи в торговых отношениях с Китаем!\n")


@dp.message_handler(text="🇺🇿Наш адрес в Ташкенте")
async def loco(message: types.Message):
    await message.answer_location(latitude=41.296685, longitude=69.21233)
    await message.answer(f"📍Наш адрес:\n"
    f"г.Ташкент Чиланзорский район 7 кв 18-дом, возле клиники \n"
                         f"Ориентир Доктор Сервис Напротив детского сада 265.\n"
                         f"☎+998909850311\n"
                         f"✉️@baraka_admin0311\n\n"
                         f"Рабочий день с понедельника по субботу\n"
                         f"Часы:9:00-18:00\n"
                         f"Выходной: воскресенье")




@dp.message_handler(text="📦Грузы без номеров")
async def kodsiz_yuklar(message: types.Message):
    await message.answer(f"Из-за ошибок при вводе адреса в Китае или недействительности штрих-кода на товаре и по "
                         f"другим причинам существует вероятность того, что ваш товар окажется без кода.\n\n"
                         f"https://t.me/btk_kodsiz_yuklar\n\n"
                         f"Отправьте админу штрих-код известного вам груза и вы сможете его забрать.\n\n"
                         f"👉 @baraka_admin0311")


