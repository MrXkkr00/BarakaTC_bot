from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.bosh_menu import id_key, vil_key, bosh_menu
from keyboards.default.bosh_menu import only_boshmenu
from keyboards.default.common import til
from loader import dp
from utils.db_api.users_sql import Database_User
db_user = Database_User()
from time import strftime, gmtime


class RegStart(StatesGroup):
    name = State()
    contact_state = State()
    add_contact = State()
    adress_viloyat = State()
    adress_kocha = State()


@dp.message_handler(text="Bosh menu")
async def only_bosh_menushu(message: types.Message):
    await message.answer(f"📲Kerakli bo'limni tanlang", reply_markup=id_key)


@dp.message_handler(text="Bosh menu", state=[RegStart.name, RegStart.contact_state, RegStart.add_contact,
                                             RegStart.adress_viloyat, RegStart.adress_kocha])
async def only_1_menushu(message: types.Message, state: FSMContext):
    await message.answer(f"📲Kerakli bo'limni tanlang", reply_markup=id_key)
    await state.finish()


@dp.message_handler(text="/start", state=[RegStart.name, RegStart.contact_state, RegStart.add_contact,
                                             RegStart.adress_viloyat, RegStart.adress_kocha])
async def onlydfsushu(message: types.Message, state: FSMContext):
    await message.answer(f"📲Kerakli bo'limni tanlang", reply_markup=til)
    await state.finish()


@dp.message_handler(text="🇺🇿 O'zbek")
async def start1(message: types.Message):
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
        await message.answer(f"📲Kerakli bo'limni tanlang", reply_markup=bosh_menu)
    else:
        await message.answer(f"Assalomu Alaykum", reply_markup=id_key)


@dp.message_handler(text="🔑ID raqam olish")
async def start1(message: types.Message):
        await message.answer(f"Ism Familyangizni kiriting : ", reply_markup=only_boshmenu)
        await RegStart.name.set()


@dp.message_handler(state=RegStart.name)
async def start2(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer(f"Telefon raqamingizni kiriting.\n"
                         f"Namuna: +998YY1234567")
    await RegStart.contact_state.set()


# contact_state
# @dp.message_handler(content_types="contact", state=RegStart.contact_state)
# async def start3(message: types.Message):
#     await message.answer(f"Qo'shimcha contact kiriting:\n"
#                          f"Masalan : 993321038", reply_markup=ReplyKeyboardRemove())
#     await RegStart.add_contact.set()


@dp.message_handler(lambda message: message.text[:4] == "+998" and len(message.text) == 13,
                    state=RegStart.contact_state)
async def con2131tact(message: types.Message, state: FSMContext):
    nomer = str(message.text)
    try:
        await db_user.create()
    except:
        pas = 1
    user = await db_user.select_user(nomer=nomer)
    if user:
        return await message.answer(f"Bu raqam oldin kiritilgan \n"
                                    f"Iltimos boshqa raqam kiriting:\n"
                                    f"Masalan : +998YY1234567")
    else:
        nomer = str(message.text)
        await state.update_data(
            {"nomer": nomer}
        )
        await message.answer(f"Qo'shimcha Telefon raqam kiriting:\n"
                             f"Masalan : +998YY1234567")
        await RegStart.add_contact.set()


@dp.message_handler(state=RegStart.contact_state)
async def start44(message: types.Message):
    return await message.answer(f"Bu yerga faqat telefon raqam kiriting:\n"
                                f"Masalan : +998YY1234567")


# qo'shimcha contact
# @dp.message_handler(content_types="contact", state=RegStart.add_contact)
# async def start33(message: types.Message):
#     await message.answer(f"Yashash viloyatingizni tanlang. : ", reply_markup=vil_key)
#     await RegStart.adress_viloyat.set()


@dp.message_handler(lambda message: message.text[:4] == "+998" and len(message.text) == 13,
                    state=RegStart.add_contact)
async def con21312tact(message: types.Message, state: FSMContext):
    qo_nomer = str(message.text)
    data = await state.get_data()
    nomer = str(data.get("nomer"))
    if nomer == qo_nomer:
        return await message.answer(f"Bu raqam oldin kiritilgan \n"
                                    f"Iltimos boshqa raqam kiriting:\n"
                                    f"Masalan : +998YY1234567")
    else:
        await state.update_data(
            {"qosh_nomer": qo_nomer}
        )
        await message.answer(f"Yashash viloyatingizni tanlang. : ", reply_markup=vil_key)
        await RegStart.adress_viloyat.set()


@dp.message_handler(state=RegStart.add_contact)
async def start41(message: types.Message):
    return await message.answer(f"Bu yerga faqat telefon raqam kiriting:\n"
                                f"Masalan : +998YY1234567", reply_markup=only_boshmenu)


# addres enter


@dp.message_handler(state=RegStart.adress_viloyat)
async def adress_12s(message: types.Message, state: FSMContext):
    viloyat = str(message.text)
    await state.update_data(
        {"viloyat": viloyat}
    )
    await message.answer(f"Yashash manzilingizni kiriting.\n\n"
                         f"Namuna: Toshkent shaxar,Chilonzor  tuman, Nurlikelajak ko'chasi 1-uy 23-xonadon",
                         reply_markup=only_boshmenu)
    await RegStart.adress_kocha.set()


@dp.message_handler(state=RegStart.adress_kocha)
async def adress_kocha(message: types.Message, state: FSMContext):
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
    mijoz.write(f"\n{user_id}    {BTK_id}    {name}    {str(nomer)}    {str(qosh_nomer)}    {viloyat}    {address}    {time}")
    mijoz.close()

    await message.answer(f"Hamkorlik qilganingiz uchun raxmat\n"
                         f"Sizga   BTK-{BTK_id}    raqami berildi\n"
                         f"Xitoy bilan savdo aloqalaringizda omad tilaymiz", reply_markup=bosh_menu)
    await state.finish()
