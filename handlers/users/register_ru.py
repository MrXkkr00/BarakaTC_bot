from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.bosh_menu_ru import *
from keyboards.default.common import til
from loader import dp
from utils.db_api.users_sql import Database_User

db_user = Database_User()
from time import strftime, gmtime


class RegStart_ru(StatesGroup):
    name = State()
    contact_state = State()
    add_contact = State()
    adress_viloyat = State()
    adress_kocha = State()


@dp.message_handler(text="Главное меню")
async def only_bosh_menushu_ru(message: types.Message):
    await message.answer(f"📲Выберите нужный раздел", reply_markup=id_key_ru)




@dp.message_handler(text="/start")
async def onlyryf_menushu_ru(message: types.Message):
    await message.answer(f"📲Выберите нужный раздел", reply_markup=id_key_ru)



@dp.message_handler(text="Главное меню", state=[RegStart_ru.name, RegStart_ru.contact_state, RegStart_ru.add_contact,
                                                RegStart_ru.adress_viloyat, RegStart_ru.adress_kocha])
async def only_1_menushu_ru(message: types.Message, state: FSMContext):
    await message.answer(f"📲Выберите нужный раздел", reply_markup=id_key_ru)
    await state.finish()


@dp.message_handler(text="/start", state=[RegStart_ru.name, RegStart_ru.contact_state, RegStart_ru.add_contact,
                                                RegStart_ru.adress_viloyat, RegStart_ru.adress_kocha])
async def only_dfsfhu_ru(message: types.Message, state: FSMContext):
    await message.answer(f"📲Выберите нужный раздел", reply_markup=til)
    await state.finish()


@dp.message_handler(text="/start", state=[RegStart_ru.name, RegStart_ru.contact_state, RegStart_ru.add_contact,
                                                RegStart_ru.adress_viloyat, RegStart_ru.adress_kocha])
async def onlyfdsfhu_ru(message: types.Message, state: FSMContext):
    await message.answer(f"📲Выберите нужный раздел", reply_markup=id_key_ru)
    await state.finish()


@dp.message_handler(text="🇷🇺 Русский")
async def start1_ru(message: types.Message):
    try:
        await db_user.create()
    except:
        pas = 1
    try:
        await db_user.create_table_users()
    except:
        pas = 1
    user = await db_user.select_user(user_id=str(message.from_user.id))
    if user:
        await message.answer(f"📲Выберите нужный раздел", reply_markup=bosh_menu_ru)
    else:
        await message.answer(f"Привет", reply_markup=id_key_ru)


@dp.message_handler(text="🔑Получить ID номер")
async def start1_ruu(message: types.Message):
    await message.answer(f"Введите свое имя и фамилию : ", reply_markup=only_boshmenu_ru)
    await RegStart_ru.name.set()


@dp.message_handler(state=RegStart_ru.name)
async def start2_ru(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer(f"Введите свой номер телефона.\n"
                         f"Пример: +998YY1234567")
    await RegStart_ru.contact_state.set()


# contact_state
# @dp.message_handler(content_types="contact", state=RegStart.contact_state)
# async def start3(message: types.Message):
#     await message.answer(f"Qo'shimcha contact kiriting:\n"
#                          f"Masalan : 993321038", reply_markup=ReplyKeyboardRemove())
#     await RegStart.add_contact.set()


@dp.message_handler(lambda message: message.text[:4] == "+998" and len(message.text) == 13,
                    state=RegStart_ru.contact_state)
async def con2131tact_ru(message: types.Message, state: FSMContext):
    nomer = str(message.text)
    try:
        await db_user.create()
    except:
        pas = 1
    user = await db_user.select_user(nomer=nomer)
    if user:
        return await message.answer(f"Этот номер был введен ранее\n"
                                    f"Пожалуйста, введите другой номер:\n"
                                    f"Например: +998YY1234567")
    else:
        nomer = str(message.text)
        await state.update_data(
            {"nomer": nomer}
        )
        await message.answer(f"Введите дополнительный номер телефона:\n"
                             f"Например: +998YY1234567")
        await RegStart_ru.add_contact.set()


@dp.message_handler(state=RegStart_ru.contact_state)
async def start44_ru(message: types.Message):
    return await message.answer(f"Введите здесь только номер телефона:\n"
                                f"Например: +998YY1234567")


# qo'shimcha contact
# @dp.message_handler(content_types="contact", state=RegStart.add_contact)
# async def start33(message: types.Message):
#     await message.answer(f"Yashash viloyatingizni tanlang. : ", reply_markup=vil_key)
#     await RegStart.adress_viloyat.set()


@dp.message_handler(lambda message: message.text[:4] == "+998" and len(message.text) == 13,
                    state=RegStart_ru.add_contact)
async def con21312tact_ru(message: types.Message, state: FSMContext):
    qo_nomer = str(message.text)
    data = await state.get_data()
    nomer = str(data.get("nomer"))
    if nomer == qo_nomer:
        return await message.answer(f"Этот номер был введен ранее\n"
                                    f"Пожалуйста, введите другой номер:\n"
                                    f"Например: +998YY1234567")
    else:
        await state.update_data(
            {"qosh_nomer": qo_nomer}
        )
        await message.answer(f"Выберите регион проживания : ", reply_markup=vil_key_ru)
        await RegStart_ru.adress_viloyat.set()


@dp.message_handler(state=RegStart_ru.add_contact)
async def start41_ru(message: types.Message):
    return await message.answer(f"Введите здесь только номер телефона:\n"
                                f"Например: +998YY1234567", reply_markup=only_boshmenu_ru)


# addres enter


@dp.message_handler(state=RegStart_ru.adress_viloyat)
async def adress_12s_ru(message: types.Message, state: FSMContext):
    viloyat = str(message.text)
    await state.update_data(
        {"viloyat": viloyat}
    )
    await message.answer(f"Введите адрес вашего проживания.\n\n"
                         f"Пример: город Ташкент, Чиланзорский район, улица Нурликеладжак 1, дом 23",
                         reply_markup=only_boshmenu_ru)
    await RegStart_ru.adress_kocha.set()


@dp.message_handler(state=RegStart_ru.adress_kocha)
async def adress_kocha_ru(message: types.Message, state: FSMContext):
    address = str(message.text)
    await state.update_data(
        {"address": address}
    )
    f = open("./data/reg/BTK", "r")
    BTK = f.read()
    f = open("./data/reg/BTK", "w")
    f.write(f"{int(BTK) + 1}")
    f.close()

    data = await state.get_data()
    user_id = message.from_user.id
    BTK_id = str(BTK)
    name = data.get("name")
    nomer = data.get("nomer")
    qosh_nomer = data.get("qosh_nomer")
    viloyat = data.get("viloyat")
    address = data.get("address")
    try:
        await db_user.create()
    except:
        pas = 1
    try:
        await db_user.create_table_users()
    except:
        pass
    time = str(strftime(f"%d.%m.20%y", gmtime()))
    await db_user.add_user(user_id=str(user_id), BTK_id=BTK_id, name=name, nomer=str(nomer), qosh_nomer=str(qosh_nomer),
                           viloyat=str(viloyat),
                           address=str(address),
                           vaqt=str(time))
    mijoz = open("./data/reg/users_about", "a")
    mijoz.write(
        f"\n{user_id}    {BTK_id}    {name}    {str(nomer)}    {str(qosh_nomer)}    {viloyat}    {address}    {time}")
    mijoz.close()

    await message.answer(f"Спасибо за сотрудничество\n"
                         f"Вам присвоен номер  BTK-{BTK_id}  \n"
                         f"Желаем вам удачи в торговых отношениях с Китаем", reply_markup=bosh_menu_ru)
    await state.finish()
