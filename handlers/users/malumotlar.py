from aiogram import types

from keyboards.default.bosh_menu import bosh_menu
from loader import dp, bot
from utils.db_api.users_sql import Database_User

db_user = Database_User()

@dp.message_handler(text="🏠Bosh menu")
async def bosh_menushu(message: types.Message):
    await message.answer(f"📲Kerakli bo'limni tanlang", reply_markup=bosh_menu)

@dp.message_handler(text="📑Kargo haqida malumot")
async def kargo_about(message: types.Message):
    await message.answer(f"KARGO HAQIDA MALUMOT\n"
                         f"🚚AVTO KARGO-1kg yuk uchun 7$ yetib kelish muddati Xitoy omboriga borgan kundan 15-20kun\n "
                         f"📍Viloyat filiallaridan oladiganlar uchun 7$\n"
                         f"Minimalka yoʻq\n"
                         f"Gabarit bor\n"
                         f"✈️ AVIA KARGO -1kg yuk uchun 11,5$\n"
                         f"Upakovka kunidan boshlab 7-10kun\n"
                         f"Minimalka bor\n"
                         f"Gabarit bor\n"
                         f"‼️Xitoydan olib kirish mumkin boʻlmagan tovarlar roʻyxati ‼️\n"
                         f"❌Narkotik, psixotrop moddalar (sigaretalar, kalyan tamaki).\n"
                         f"❌2) Alkogolli mahsulotlar.\n"
                         f"❌3) Xavfli moddalarning portlashi (salyutlar, feyerverklar, petardalar), "
                         f"shuningdek kimyoviy moddalar\n"
                         f"❌4) Provokatsion ekstremistik, kitoblar, nashrlar, materiallar jamiyatga salbiy ta'sir "
                         f"ko'rsatadigan zo'ravonlik, pornografiya, video materiallar.\n"
                         f"❌5) Tibbiy asbob-uskunalar va asboblar, dori-darmonlar, "
                         f"dorivor preparatlar (o'tlar, malhamlar, vitaminlar, balzamlar, preparatlar).\n"
                         f"❌6) Kosmetologiya uskunalari (zarb, igna, shprits).\n"
                         f"❌7) Lazer ko'rsatkichlari (lazer nurlarini ko'paytirish).\n"
                         f"❌8) Dronlar (samolyotlar).\n"
                         f"❌9) Qimor o'yin avtomatlari (poker chiplari).\n"
                         f"❌10) Uyali telefonlar (ekrandan tashqari ehtiyot qismlar, SIM kartali planshet).\n"
                         f"❌11) Qimmatbaho metallar (oltin, kumush...)\n"
                         f"❌12) Elektr, gaz, suv hisoblagichlari\n"
                         f"❌13) Avtomobil dvigatellari.\n"
                         f"❌14) O'qotar qurollar, elektr shokerlar, pnevmatik va gazli qurollar, "
                         f"o'q otish uchun patronlar (patronlar, kamon va o'qlar).\n"
                         f"❌15) Intim o'yinchoqlar, qo'g'irchoqlar (stimulyatorlar, malhamlar).\n"
                         f"❌16) rekvizitsiz oziq-ovqat yorliqlari.\n"
                         f"❌17) Boshqaruvning roziligi bilan oziq-ovqat mahsulotlari\n\n"
                         f"✈️ Aviada yuqoridagi tovarlar bilan birga ❌️❌️❌\n\n"
                         f"Batareykali narsalar 🔋🪫\n"
                         f"Magniti bor narsalar ⚙️\n"
                         f"Har qanday suyuqliklar 💦\n"
                         f"Linzalar 👁\n"
                         f"Kleylar 💥\nPoroshok, kukunli narsalar \n"
                         f"MUMKIN EMAS ❌\n\n"
                         f"🚫  Iltimos, shunaqa yuklarni aviaga urib qo'ymang ‼️")

    await message.answer(f"Asosiy yangiliklarni guruhimizda kuzatib boring\n"
                         f"👉https://t.me/barakatezkor_cargo\n\n"
                         f"Darsliklar guruhimizni kuzatib boring\n"
                         f"👉https://t.me/barakakargo_darslik") 


@dp.message_handler(text="☎Call Center")
async def call_centeruchun(message: types.Message):
    photo = open("./data/RASM/call_center.jpg", "rb")
    await message.answer_photo(photo=photo)


@dp.message_handler(text="📱Id raqam va Adress olish")
async def id_adress_olish(message: types.Message):
    try:
        await db_user.create()
    except:
        pas = 1
    user = await db_user.select_user(user_id=str(message.from_user.id))
    btk = user[2]
    video = open("./data/video.mp4", "rb")
    await bot.send_video(message.chat.id, video=video)
    await message.answer(f"Sizga   BTK-{btk}    raqami berildi!")
    await message.answer(f"Bizning Xitoydagi omborimiz manzili:")
    await message.answer(f"联系电话：15267397101\n"
                               f"浙江省，金华市，义乌市，稠城街道，兴港小区152幢二单元一楼门面")
    await message.answer(f"Biz bilan hamkorlik qilganingiz uchun Raxmat "
                               f"Xitoy bilan savdo aloqalaringizda omad tilaymiz!")
    # await db_user.update_user_btk(BTK_id="162", id=159)    
    # await db_user.update_user_btk(BTK_id="163", id=160)


@dp.message_handler(text="🇺🇿Toshkentdagi manzilimiz")
async def loco(message: types.Message):
    await message.answer_location(latitude=41.296685, longitude=69.21233)
    await message.answer(f"📍Bizning manzilimiz:\n "
                         f"Toshkent shahar Chilonzor tumani 7kv 18-dom,Orientir Doktor Servis klinikasi yaqinida, 265-bogʻcha roʻparasida\n"
                         f"☎+998909850311\n"
                         f"✉@baraka_admin0311\n\n"
                         f"Ish kuni Dushanbadan-Shanbagacha\n"
                         f"Soat: 9:00-18:00\n"
                         f"Dam olish kuni:Yakshanba")




@dp.message_handler(text="📦Kodsiz yuklar")
async def kodsiz_yuklar(message: types.Message):
    await message.answer(f"Xitoy manzilini kiritishda xatoliklar tufayli yoki tovar ustidagi shtrix qogʻozi "
                         f"yaroqsiz holga kelganida va boshqa sabablarda tovaringiz kodsiz boʻlib kelishi extimoli "
                         f"bor Uzoq muddat ichida yuklarizni olishda muammoga duch kelsangiz shu guruhda kodsiz yuklar"
                         f" roʻyxatini kuzatib boring izlayotgan tovarizni topishingiz mumkin\n\n"
                         f"https://t.me/btk_kodsiz_yuklar\n\n"
                         f"Sizga tanish boʻlgan yuk shtrix kodini adminga yuboring mos kelsa olib ketishingiz mumkin\n"
                         f"👉 @baraka_admin0311")


