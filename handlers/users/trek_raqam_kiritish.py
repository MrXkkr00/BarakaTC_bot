from time import gmtime, strftime

import xlsxwriter
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.bosh_menu import bosh_menu
from keyboards.default.bosh_menu_ru import bosh_menu_ru
from keyboards.default.common import til
from loader import dp, bot
from utils.db_api.trek_nomer_sql import Database_Trek_nomer
from utils.db_api.users_sql import Database_User

db_user = Database_User()
db_trek = Database_Trek_nomer()


class Trek_raqam_ru(StatesGroup):
    trek = State()
class Trek_raqam(StatesGroup):
    trek = State()

@dp.message_handler(commands=['start'], state=[Trek_raqam.trek, Trek_raqam_ru.trek])
async def handle_start(message: types.Message, state: FSMContext):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup=til)




@dp.message_handler(text="🚚Trek raqam kiritish AVTO")
async def trek_Reqad(message: types.Message):
    await message.answer(f"Trek raqamingizni kiriting : ", reply_markup=ReplyKeyboardRemove())
    await Trek_raqam.trek.set()


@dp.message_handler(state=Trek_raqam.trek)
async def trek213qad(message: types.Message, state: FSMContext):
    try:
        await db_trek.create_table_users()
    except:
        pas = 1

    try:
        await db_trek.create()
    except:
        pas = 1
    try:
        await db_user.create()
    except:
        pas = 1
    trek_nomer = str(message.text)
    user_id = str(message.from_user.id)
    user = await db_user.select_user(user_id=user_id)
    time = str(strftime(f"%d.%m.20%y", gmtime()))
    await db_trek.add_user(user_id=user_id, BTK_id=user[2], name=user[3], trek_nomer=trek_nomer, time_enter=time)

    await message.answer(f"Trek raqamigiz qabul qilindi.", reply_markup=bosh_menu)
    await state.finish()





@dp.message_handler(text="🚚Ввод номера трека АВТО")
async def trek_R21313eqad(message: types.Message):
    await message.answer(f"Введите свой трек-номер : ", reply_markup=ReplyKeyboardRemove())
    await Trek_raqam_ru.trek.set()


@dp.message_handler(state=Trek_raqam_ru.trek)
async def tr13213ek213qad(message: types.Message, state: FSMContext):
    try:
        await db_trek.create_table_users()
    except:
        pas = 1

    try:
        await db_trek.create()
    except:
        pas = 1
    try:
        await db_user.create()
    except:
        pas = 1
    trek_nomer = str(message.text)
    user_id = str(message.from_user.id)
    user = await db_user.select_user(user_id=user_id)
    time = str(strftime(f"%d.%m.20%y", gmtime()))
    await db_trek.add_user(user_id=user_id, BTK_id=user[2], name=user[3], trek_nomer=trek_nomer, time_enter=time)

    await message.answer(f"Ваш трек-номер получен.", reply_markup=bosh_menu_ru)
    await state.finish()


@dp.message_handler(text="/trek_raqamlar")
async def reg_uchun(message: types.Message, state: FSMContext):
    try:
        await db_trek.create()
    except:
        pas = 1
    try:
        await db_trek.create_table_users()
    except:
        pas = 1

    workbook = xlsxwriter.Workbook(f'data/Exel/Trek_nomerlar.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', "№")
    worksheet.write('B1', "Trek")
    worksheet.write('C1', "BTK ID")
    worksheet.write('D1', "Ism Familya")
    worksheet.write('E1', "Vaqt")


    # try:
    users = await db_trek.select_all_users()

    for i in range(len(users)):
        # print(f"user_id", users[i][1])
        # print(f"btk", users[i][2])
        # print(f"name", users[i][3])
        # print(f"nomer", users[i][4])
        # print(f"qoshim_nomer", users[i][5])
        # print(f"qoshim_nomer", users[i][6])
        # print(f"manzil", users[i][7])
        # print(f"time", users[i][8])

        # worksheet.write('A1', "№")
        worksheet.write(f'A{i + 2}', users[i][0])
        worksheet.write(f'B{i + 2}', users[i][4])
        worksheet.write(f'C{i + 2}', f"BTK-{users[i][2]}")
        worksheet.write(f'D{i + 2}', users[i][3])
        worksheet.write(f'E{i + 2}', users[i][5])


    # except:
    #     pas=1
    workbook.close()
    with open(f"data/Exel/Trek_nomerlar.xlsx", "rb") as photo_file:
        await bot.send_document(chat_id=message.from_user.id, document=photo_file)


