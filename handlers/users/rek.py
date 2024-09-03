from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users.register import RegStart
from keyboards.default.common import til
from loader import dp, bot


@dp.message_handler(text="/start")
async def bot_start(message: types.Message):
    photo = open("./data/RASM/Logo.jpg", "rb")
    await message.answer_photo(photo=photo, caption=f"Baraka Tezkor Kargo orqali roʻyxatdan oʻtishingizdan avval shartlar bilan tanishib chiqing\n"
                                                    f"*Kelgusida baʼzi muammolarga uchramaslik uchun bitta mobil "
                                                    f"raqamdan va telegram akkauntidan faqat bir martda roʻyxatdan oʻtishingiz mumkin\n"
                                                    f"*Shunday ekan malumotlaringizni kiritishda asosiy raqamingiz va "
                                                    f"akkauntingizdan foydalaning\n"
                                                    f"*Maʼlumotlarni kiritishda xatolarga yoʻl qoʻymasligingizni "
                                                    f"soʻraymiz\n") 
    user_id = message.from_user.id
    f = open("./data/reg/reklama.txt", "r")
    text = f.read()
    if not str(user_id) in text:
        f = open("./data/reg/reklama.txt", "a")
        f.write(f"{str(user_id)}\n")
        f.close()
    await message.answer(f"Assalomu Alaykum!", reply_markup=til)


@dp.message_handler(text="/start",
                    state=[RegStart.name, RegStart.contact_state, RegStart.add_contact, RegStart.adress_viloyat,
                           RegStart.adress_kocha])
async def bot_start2(message: types.Message):
    photo = open("./data/RASM/Logo.jpg", "rb")
    await message.answer_photo(photo=photo, caption=f"Baraka Tezkor Kargo orqali roʻyxatdan oʻtishingizdan avval shartlar bilan tanishib chiqing\n"
                                                    f"*Kelgusida baʼzi muammolarga uchramaslik uchun bitta mobil "
                                                    f"raqamdan va telegram akkauntidan faqat bir martda roʻyxatdan oʻtishingiz mumkin\n"
                                                    f"*Shunday ekan malumotlaringizni kiritishda asosiy raqamingiz va "
                                                    f"akkauntingizdan foydalaning\n"
                                                    f"*Maʼlumotlarni kiritishda xatolarga yoʻl qoʻymasligingizni "
                                                    f"soʻraymiz\n") 
    await message.answer(f"Assalomu Alaykum!", reply_markup=til)


class Reklama_State(StatesGroup):
    text = State()


@dp.message_handler(text_contains="//reklama")
async def bot2342_start(message: types.Message, state: FSMContext):
    msg = message.text[9:]
    await state.update_data(
        {"msg": msg}
    )

    await message.answer(f"Rasm yuboring")
    await Reklama_State.text.set()


@dp.message_handler(content_types=["photo"], state=Reklama_State.text)
async def bot_text(message: types.Message, state: FSMContext):
    document_id = message.photo[0].file_id
    file_info = await bot.get_file(document_id)
    data = await state.get_data()
    msg = data.get("msg")
    f = open("./data/reg/reklama.txt", "r")
    text = f.read()
    id = ""
    for i in range(len(text)):
        try:
            if (not text[i] == f"\n"):
                id += text[i]
            else:
                await bot.send_photo(chat_id=int(id), photo=file_info.file_id, caption=msg)
                id = ""
        except:
            pass

    await state.finish()


@dp.message_handler(text="//count")
async def bot22_start(message: types.Message):
    f = open("./data/reg/reklama.txt", "r")
    text = f.read()
    sum = 0
    for i in range(len(text)):
        if text[i] == f"\n":
            sum = sum + 1
    await message.answer(f"{sum}")
