from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardMarkup, InlineKeyboardButton  
from datetime import datetime, timedelta
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

 
# клавиатура начальной точки
sinline_btn_1 = InlineKeyboardButton('ДУ Пятёрочка', callback_data='sДУ Пятёрочка')
sinline_btn_2 = InlineKeyboardButton('ДУ Парина', callback_data='sДУ Парина')
sinline_btn_3 = InlineKeyboardButton('УНИКС/Главное здание/Двойка', callback_data='sУНИКС/Главное здание/Двойка')
sinline_btn_4 = InlineKeyboardButton('Кремлевская 6', callback_data='sКремлевская 6')
sinline_btn_5 = InlineKeyboardButton('Межлаука 1/Москва', callback_data='sМежлаука 1/Москва')
sinline_btn_6 = InlineKeyboardButton('Бутлерова 4', callback_data='sБутлерова 4')
sinline_btn_7 = InlineKeyboardButton('Оренбургский тракт 10а', callback_data='sОренбургский тракт 10а')
sinline_btn_8 = InlineKeyboardButton('Бустан', callback_data='sБустан')
sinline_btn_9 = InlineKeyboardButton('Татарстан 2/Пушкина 1', callback_data='sТатарстан 2/Пушкина 1')
sinline_btn_10 = InlineKeyboardButton('Аэропорт', callback_data='sАэропорт')

sinline_kb = InlineKeyboardMarkup().add(sinline_btn_1, sinline_btn_2).add(sinline_btn_3).add(sinline_btn_5,sinline_btn_6).add(sinline_btn_4,sinline_btn_8).add(sinline_btn_9).add(sinline_btn_7).add(sinline_btn_10)


# клавиатура конечной точки 
finline_btn_1 = InlineKeyboardButton('ДУ Пятёрочка', callback_data='fДУ Пятёрочка')
finline_btn_2 = InlineKeyboardButton('ДУ Парина', callback_data='fДУ Парина')
finline_btn_3 = InlineKeyboardButton('УНИКС/Главное здание/Двойка/Физфак', callback_data='fУНИКС/Главное здание/Двойка/Физфак')
finline_btn_4 = InlineKeyboardButton('Кремлевская 6', callback_data='fКремлевская 6')
finline_btn_5 = InlineKeyboardButton('Межлаука 1/Москва', callback_data='fМежлаука 1/Москва')
finline_btn_6 = InlineKeyboardButton('Бутлерова 4', callback_data='fБутлерова 4')
finline_btn_7 = InlineKeyboardButton('Оренбургский тракт 10а', callback_data='fОренбургский тракт 10а')
finline_btn_8 = InlineKeyboardButton('Бустан', callback_data='fБустан')
finline_btn_9 = InlineKeyboardButton('Татарстан 2/Пушкина 1', callback_data='fТатарстан 2/Пушкина 1')
finline_btn_10 = InlineKeyboardButton('Аэропорт', callback_data='fАэропорт')



finline_kb = InlineKeyboardMarkup().add(finline_btn_1, finline_btn_2).add(finline_btn_3).add(finline_btn_5,finline_btn_6).add(finline_btn_4,finline_btn_8).add(finline_btn_9).add(finline_btn_7).add(finline_btn_10)



# функция создающая клавиатуру времени отправления
def time_kb():
    volue_timebtn_1 = str(datetime.now().strftime("%H:%M") + "-" + sum_time(0,10))
    volue_timebtn_2 = str(sum_time(0,10) + "-" + sum_time(0,20))
    volue_timebtn_3 = str(sum_time(0,20) + "-" + sum_time(0,30))
    volue_timebtn_4 = str(sum_time(0,30) + "-" + sum_time(0,40))
    volue_timebtn_5 = str(sum_time(0,40) + "-" + sum_time(0,50))
    volue_timebtn_6 = str(sum_time(0,50) + "-" + sum_time(0,60))
    timeinline_btn_1 = InlineKeyboardButton(volue_timebtn_1, callback_data='timeinterval'+volue_timebtn_1)
    timeinline_btn_2 = InlineKeyboardButton(volue_timebtn_2, callback_data='timeinterval'+volue_timebtn_2)
    timeinline_btn_3 = InlineKeyboardButton(volue_timebtn_3, callback_data='timeinterval'+volue_timebtn_3)
    timeinline_btn_4 = InlineKeyboardButton(volue_timebtn_4, callback_data='timeinterval'+volue_timebtn_4)
    timeinline_btn_5 = InlineKeyboardButton(volue_timebtn_5, callback_data='timeinterval'+volue_timebtn_5)
    timeinline_btn_6 = InlineKeyboardButton(volue_timebtn_6, callback_data='timeinterval'+volue_timebtn_6)

    time_inline_kb =  InlineKeyboardMarkup(row_width=3).add(timeinline_btn_1, timeinline_btn_2, timeinline_btn_3, timeinline_btn_4, timeinline_btn_5, timeinline_btn_6)
    return time_inline_kb

# клавиатура заполнить заново 
markup_request_zapolnit_again = ReplyKeyboardMarkup(resize_keyboard=True).add(# клавиатура выходящая после поиска попутчиков
    KeyboardButton('Заполнить анкету заново🔄'))




# клавитура ссылка
keyboard_url = InlineKeyboardMarkup()
button = InlineKeyboardButton('Инструкция как это сделать', url='https://telegram-pro.ru/kak-pomenyat-imya-v-telegramme-instruktsiya-po-primeneniyu/')
keyboard_url.add(button)


# "https://geek-help.ru/kak-sdelat-imya-polzovatelya-v-telegram/#:~:text=%D0%BD%D0%B0%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%2C%20%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D0%B2%20%D1%86%D0%B8%D1%84%D1%80%D1%8B.-,%D0%9A%D0%B0%D0%BA%20%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C%20%D0%B8%D0%BC%D1%8F%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F%20%D0%B2%20%D0%A2%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC%20%D1%81%20%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD%D0%B0,%D0%A1%D1%80%D0%B0%D0%B7%D1%83%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D1%8D%D1%82%D0%BE%D0%B3%D0%BE%20%D0%B8%D0%BC%D1%8F%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F%20%D0%B1%D1%83%D0%B4%D0%B5%D1%82%20%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%BE.,-%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%B8%D1%82%D0%B5%20%D0%B2%D0%BD%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D0%B5
# клавиатура выходящая после поиска попутчиков
markup_request_start = ReplyKeyboardMarkup(resize_keyboard=True).add(# клавиатура выходящая после поиска попутчиков
    KeyboardButton('Заполнить анкету заново🔄'),KeyboardButton('Выбрать другое время⏰') ).add(KeyboardButton('Повторить попытку поиска попутчиков🔎')).add(KeyboardButton('Я нашел попутчиков, выключите мою анкету⛔️'))

# клавиатура после отлова неизвестных сообщений
markup_request_unknown_message = ReplyKeyboardMarkup(resize_keyboard=True).add(# клавиатура выходящая после поиска попутчиков
    KeyboardButton('Заполнить анкету заново🔄'),KeyboardButton('Помощь🆘'))
# кнопка для получения контакта
markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add( # кнопка для получения контакта
    KeyboardButton('Отправить свой контакт✅', request_contact=True),KeyboardButton('Я не хочу делиться своим номером❌')
)
# кнопка для ввода времени вручную
markup_request_time = ReplyKeyboardMarkup(resize_keyboard=True).add( # кнопка для ввода времени вручную
    KeyboardButton('Указать своё время⏰')
)



# оперативка чтоб хранить состояния 
storage = MemoryStorage()# оперативка чтоб хранить состояния 


# классы для работы с состояниями(хуй знает как это работает =) )
class Form(StatesGroup):
    time = State()
class Mail(StatesGroup):
    mass_mailing = State()


# иденцифицируем бота
bot = Bot(token='5264359095:AAGIRxsQKXFPgJYmxsAv2NSg20gIUG4_6AY')# иденцифицируем бота
dp = Dispatcher(bot, storage = storage) 



# создание таблицы в БД
conn = sqlite3.connect('orders.db') # создание таблицы в БД
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
              (userid INT, username TEXT, start TEXT, finish TEXT,  fTime INT, sTime INT, time_str TEXT )''')


# 1.0
# хэндлер STARTa 
@dp.message_handler(commands=['start'] ) # хэндлер STARTa 
async def process_start_command(message: types.Message):
    deleter(message.chat.id)
    try:
        await bot.send_message(message.chat.id, "Заполним анкету!", reply_markup=types.ReplyKeyboardRemove())
    except:
        await asyncio.sleep(0.1)
    userid_setter(message.from_user.id)
    if message.from_user.username == None:
# \nЕсли вдруг не хочешь распространять свой номер - укажи имя пользовтеля. Подробное руководство, о том, как это можно сделать <a href="https://geek-help.ru/kak-sdelat-imya-polzovatelya-v-telegram/#:~:text=%D0%BD%D0%B0%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%2C%20%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D0%B2%20%D1%86%D0%B8%D1%84%D1%80%D1%8B.-,%D0%9A%D0%B0%D0%BA%20%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C%20%D0%B8%D0%BC%D1%8F%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F%20%D0%B2%20%D0%A2%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC%20%D1%81%20%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD%D0%B0,%D0%A1%D1%80%D0%B0%D0%B7%D1%83%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D1%8D%D1%82%D0%BE%D0%B3%D0%BE%20%D0%B8%D0%BC%D1%8F%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F%20%D0%B1%D1%83%D0%B4%D0%B5%D1%82%20%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%BE.,-%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%B8%D1%82%D0%B5%20%D0%B2%D0%BD%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D0%B5">тут</a> '''
#   parse_mode=types.ParseMode.HTML)
        try:
            await bot.send_message(message.from_user.id, '''У тебя нет имени пользователя😨\n\nПоделись своим контактом для связи с попутчиками''', reply_markup=markup_request)
        except:
            await asyncio.sleep(0.1)
    else: 
        username_setter(message.from_user.id,"@" + message.from_user.username)
        try:
            # await bot.send_message(message.chat.id, '''🅂    🅃    🄰    🅁    🅃''')
            await bot.send_message(message.chat.id, '''🟢    S    T    A    R    T    🟢\n\nВыбери начальную точку ''', reply_markup=sinline_kb)
        except:
            await asyncio.sleep(0.1)



@dp.message_handler(lambda message: message.text == "Я не хочу делиться своим номером❌")
async def does_not_want_share_contact(message: types.Message):
    await bot.send_message(message.from_user.id,'''Тогда создадим имя пользователя для связи с попутчиками. Это очень просто!

⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️''', reply_markup=keyboard_url)
    await bot.send_message(message.from_user.id,"⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️",  reply_markup= ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Заполнить анкету заново🔄')))




# 1.1
# хэндлер номер пользователя при отсуствие юзернейма
@dp.message_handler(content_types=types.ContentType.CONTACT) # вот эта строка для отлавливания sharing'a номером
async def test(message: types.Message):
    try:
        await bot.send_message(message.chat.id, "Ты успешно поделился своим контактом!\nТвой номер: "+ message.contact.phone_number, reply_markup=types.ReplyKeyboardRemove())
    except:
        await asyncio.sleep(0.1)
    username_setter(message.chat.id, message.contact.phone_number)
    try:
        # await bot.send_message(message.chat.id, '''🅂    🅃    🄰    🅁    🅃''')
        await bot.send_message(message.chat.id, '''🟢    S    T    A    R    T    🟢\n\nВыбери начальную точку''', reply_markup=sinline_kb)
    except:
        await asyncio.sleep(0.1)





# 2.0
# хэндлер стартовой точки 
@dp.callback_query_handler(lambda c:  c.data and c.data.startswith('s'))# хендлер старотовй точки
async def process_callback_button_start(callback_query: types.CallbackQuery):
    try:
        await bot.answer_callback_query(callback_query.id)
    except:
        await asyncio.sleep(0.1)
    start_setter(callback_query.from_user.id,callback_query.data[1::])
    try:
        # await bot.send_message(callback_query.from_user.id,'🄵    🄸    🄽    🄸    🅂    🄷')
        await bot.send_message(callback_query.from_user.id, '🔴    F    I    N    I    S    H    🔴\n\nА теперь конечную', reply_markup=finline_kb)
    except:
        await asyncio.sleep(0.1)

# 🆂 🆃🆁🅵🅸🅽🅷                                                                   🆂 🆃 🅐 🆁 🆃
# 🅐 🅑 🅒 🅓 🅔 🅕 🅖 🅗 🅘 🅙 🅚 🅛 🅜 🅝 🅞 🅟 🅠 🅡 🅢 🅣 🅤 🅥 🅦 🅧 🅨 🅩             🅢 🅣 🅐 🅡 🅣
# Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ     Ⓢ Ⓣ Ⓐ Ⓡ Ⓣ    Ⓕ Ⓘ Ⓝ Ⓘ Ⓢ Ⓗ
# 🄰 🄱 🄲 🄳 🄴 🄵 🄶 🄷 🄸 🄹 🄺 🄻 🄼 🄽 🄾 🄿 🅀 🅁 🅂 🅃 🅄 🅅 🅆 🅇 🅈 🅉                     🅂 🅃 🄰 🅁 🅃       🄵 🄸 🄽  🄸 🅂  🄷
# Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ

# 3.0
# хэндлер финальной точки
@dp.callback_query_handler(lambda c:  c.data and c.data.startswith('f')) # хэндлер финальной точки
async def process_callback_button_finish(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    finish_setter(callback_query.from_user.id, callback_query.data[1::])
    if start_getter(callback_query.from_user.id) == callback_query.data[1::]:
        try:
            await bot.send_message(callback_query.from_user.id, "Конечная точка не может совпадать с начальной, попробуй еще разок!")
            await bot.send_message(callback_query.from_user.id, '''🟢    S    T    A    R    T    🟢\n\nВыбери начальную точку:''', reply_markup=sinline_kb)
        except:
            await asyncio.sleep(0.1)
        return 
    try:
        await bot.send_message(callback_query.from_user.id, "Твой маршрут 🚀:\n\n" + start_getter(callback_query.from_user.id) +" —> "+ callback_query.data[1::], reply_markup= markup_request_time)
    except:
        await asyncio.sleep(0.1)
    time_inline_kb = time_kb() 
    try:
        await bot.send_message(callback_query.from_user.id, "Выбери время отправления:", reply_markup=time_inline_kb)
    except:
        await asyncio.sleep(0.1)

# хэндлер выбрать другое время
@dp.message_handler(lambda message: message.text == "Выбрать другое время⏰")
async def choose_time_period_one_more(message: types.Message):
    await choose_time_period(message)
# 4.05



# хэндлер кнопки "Выбрать своё время"
@dp.message_handler(lambda message: message.text == "Указать своё время⏰")# хэндлер кнопки "Выбрать своё время"
async def choose_time_period(message: types.Message):
    try:
        await bot.send_message(message.chat.id,"Отправь временной период в формате ЧЧ:ММ-ЧЧ:ММ\n\nК примеру 20:30-21:05 или 09:05-09:45", reply_markup=types.ReplyKeyboardRemove())
    except:
        await asyncio.sleep(0.1)
    await Form.time.set()


# 4.1
# хэндлер времени написанного вручную 
@dp.message_handler(state=Form.time)# хэндлер времени написанного вручную 
async def process_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['data'] = message.text
    #  обрабатываем случай если вдруг захотят другую команду 
    if message.text == '/start':
        await state.finish()
        await process_start_command(message)
        return
    user_message = message.text
    flag = 'EROR'
    if len(user_message)==11 and  user_message[2]==':' and user_message[8]==':' and user_message[5]=='-':
        if   (0 <= int(user_message[:2:]) < 24) and (0 < int(user_message[6:8:]) <= 24) and (0 <= int(user_message[3:5:]) < 60) and (0 <= int(user_message[9:11:]) < 60):
            if ((int(user_message[3:5:]) <= int(user_message[9:11:])) and (int(user_message[:2:]) <= int(user_message[6:8:]))) or ((int(user_message[3:5:]) > int(user_message[9:11:])) and (int(user_message[:2:]) < int(user_message[6:8:]))):
                flag = 1
    try:
        f1 =int(user_message[:2:]) 
        f2 = int(user_message[3:5:]) 
        f3 = int(user_message[9:11:]) 
        f4 = int(user_message[6:8:]) 
        f5 = int(flag)
    except Exception:
        try:
            await bot.send_message(message.chat.id, "Формат не соотвествует. Попробуй еще разок!")
        except:
            await asyncio.sleep(0.1)
        return
    else:
        time_str_setter(message.chat.id,user_message)
        first_hours_in_minutes = int(user_message[:2:])* 60 
        first_minutes = int(user_message[3:5:]) 
        fTime = first_hours_in_minutes+ first_minutes
        fTime_setter(message.chat.id, fTime)

        second_hours_in_minutes = int(user_message[6:8:])* 60 
        second_minutes = int(user_message[9:11:])
        sTime = second_hours_in_minutes+second_minutes
        sTime_setter(message.chat.id, sTime)
        if (sTime - fTime) > 120:
            try:
                await bot.send_message(message.chat.id, "Слишком большой интервал! Используйте другое время")
            except:
                await asyncio.sleep(0.1)
            return
        await state.finish()
    
    
    # выбираем и выводим подходящие 
    await giving_suitable_users(message.chat.id) 
    



# 4.2
# хэндлер времени отправления
@dp.callback_query_handler(lambda c:  c.data and c.data.startswith('timeinterval'))# хэндлер времени отправления
async def process_callback_time_inline(callback_query: types.CallbackQuery): 
    await bot.answer_callback_query(callback_query.id)
    
    fTime_str_version = callback_query.data[12:17:]
    first_hours_in_minutes = int(fTime_str_version[:2:])* 60 
    first_minutes = int(fTime_str_version[3::]) 
    fTime = first_hours_in_minutes+ first_minutes
    fTime_setter(callback_query.from_user.id, fTime)

    sTime_str_version = callback_query.data[18::]
    time_str_setter(callback_query.from_user.id,  fTime_str_version+'-'+sTime_str_version)
    second_hours_in_minutes = int(sTime_str_version[:2:])* 60 
    second_minutes = int(sTime_str_version[3::])
    sTime = second_hours_in_minutes+second_minutes
    sTime_setter(callback_query.from_user.id,sTime)
    # выбираем подхоящие 
    await giving_suitable_users(callback_query.from_user.id)




# ST\


# 5.0
# хэндлер 'Я нашел попутчиков, выключите мою анкету'
@dp.message_handler(lambda message: message.text == "Я нашел попутчиков, выключите мою анкету⛔️")# хэндлер 'Я нашел попутчиков, выключите мою анкету'
async def process_START_command(message: types.Message):
    deleter(message.chat.id)
    userid_setter(message.chat.id)
    username_setter(message.chat.id,"@"+ message.chat.username)
    try:
        await bot.send_message(message.chat.id,"Твоя анкета больше неактивна!", reply_markup=markup_request_unknown_message)
    except:
        await asyncio.sleep(0.1)

# 5.1
# хэндлер 'Поторить попытку поиска попутчиков'
@dp.message_handler(lambda message: message.text == "Повторить попытку поиска попутчиков🔎")# хэндлер 'Поторить попытку поиска попутчиков'
async def process_START_command(message: types.Message):
        await giving_suitable_users(message.chat.id)


# 5.2
# хэндлер Заполнить заново
@dp.message_handler(lambda message: message.text == "Заполнить анкету заново🔄")  # хэндлер Заполнить заново  
async def process_START_command(message: types.Message):
    await process_start_command(message)


# хэндлер помощь
@dp.message_handler(lambda message: message.text == "Помощь🆘")  # хэндлер Заполнить заново  
async def process_help_command(message: types.Message):
    try:
        await bot.send_message(message.chat.id,'''Привет, студент 🙃
Я найду для тебя попутчиков в такси.

Всё просто 🚕

1. Выбираешь точку старта, финиша и удобное время

2. Получаешь контакт подходящих пользователей''', reply_markup=markup_request_zapolnit_again)
    except:
        await asyncio.sleep(0.1)


        
# массовая рассылка
@dp.message_handler(lambda message: message.text == "mass_mailing")
async def mass_mailing(message:types.Message):
    print("asdasd")
    if message.chat.id == 526233352:
        await Mail.mass_mailing.set()   
    else:
        process_unknown_comands(message)

# массовая рассылка с STATE
@dp.message_handler(state=Mail.mass_mailing)
async def process_mass_mailing(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['data'] = message.text
    print("asdasd")
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    arr_of_all_users = cur.fetchall()
    for user in arr_of_all_users:
        try:
            await bot.send_message(user[0],message.text)
        except:
            await asyncio.sleep(0.1)
    await state.finish()


# неизвестные сообщения 
@dp.message_handler(content_types=types.ContentType.ANY)
async def process_unknown_comands(message: types.Message):
    try:
        await bot.send_message(message.chat.id,"КХМ.. Не понимаю о чем ты🤔\n\nНажми на одну из кнопок, а там разберемся",reply_markup=markup_request_unknown_message)
    except:
        await asyncio.sleep(0.1)





# финалная функция выводящая ответ 
async def giving_suitable_users(id:int):
    fTime = fTime_getter(id)
    sTime = sTime_getter(id)
    arr_of_suitable_users = selector_with_timePeriod(fTime, sTime, id)
    if len(arr_of_suitable_users) == 0:
        try:
            await bot.send_message(id, "Пока попутчики не найдены😕\n\nПопробуй повторить поиск позже или дождись, пока они сами с тобой свяжутся", reply_markup=markup_request_start)
        except:
            await asyncio.sleep(0.1)
    else:
        for i in arr_of_suitable_users:
            try:
                await bot.send_message(id,  'Нашел тебе попутчика! Скорее свяжись с ним - ' + i[1]+"\nВремя его отправления - "+time_str_getter(userid_getter(i[1])), reply_markup=markup_request_start)
            except:
                await asyncio.sleep(0.1)



# выкидываем повторяющиеся ID
def deleter(userid):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    # удаляем повторяющиеся id 
    cur.execute(f'''DELETE FROM users WHERE userid= "{userid}" ''')
    conn.commit()


# сеттеры полей в БД
def userid_setter(userid:int):# сеттеры полей в БД
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    # заносим в БД данные     
    cur.execute(f'INSERT INTO users (userid) VALUES("{userid}")')
    conn.commit()
def username_setter(userid:int, username:str):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    # заносим в БД данные     
    cur.execute(f'UPDATE users SET username = "{username}" where userid = "{userid}"')
    conn.commit()
def start_setter(userid:int, start:str):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    # заносим в БД данные     
    cur.execute(f'UPDATE users SET start = "{start}" where userid = "{userid}"')
    conn.commit()
def finish_setter(userid:int, finish:str):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    # заносим в БД данные     
    cur.execute(f'UPDATE users SET finish = "{finish}" where userid = "{userid}"')
    conn.commit()
def fTime_setter(userid:int, fTime:str):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    # заносим в БД данные     
    cur.execute(f'UPDATE users SET fTime = "{fTime}" where userid = "{userid}"')
    conn.commit()
def sTime_setter(userid:int, sTime:str):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    # заносим в БД данные     
    cur.execute(f'UPDATE users SET sTime = "{sTime}" where userid = "{userid}"')
    conn.commit()
def time_str_setter(userid:int, time_str:str):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    # заносим в БД данные     
    cur.execute(f'UPDATE users SET time_str = "{time_str}" where userid = "{userid}"')
    conn.commit()
# 758821428 


# геттеры для полей из БД
def userid_getter(username):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor() 
    cur.execute(f'SELECT `userid` FROM users WHERE username = "{username}"')
    return int(cur.fetchall()[0][0])
def start_getter(userid):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor() 
    cur.execute(f'SELECT `start` FROM users WHERE userid = "{userid}"')
    return str(cur.fetchall()[0][0])
def finish_getter(userid):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor() 
    cur.execute(f'SELECT `finish` FROM users WHERE userid = "{userid}"')
    return str(cur.fetchall()[0][0])
def sTime_getter(userid):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor() 
    cur.execute(f'SELECT `sTime` FROM users WHERE userid = "{userid}"')
    return int(cur.fetchall()[0][0])
def fTime_getter(userid):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor() 
    cur.execute(f'SELECT `fTime` FROM users WHERE userid = "{userid}"')
    return int(cur.fetchall()[0][0])
def time_str_getter(userid):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor() 
    cur.execute(f'SELECT `time_str` FROM users WHERE userid = "{userid}"')
    
    return cur.fetchall()[0][0]



# функия складывающая текущее  и переданное время 
def sum_time(delhours:int, delminutes:int):
    nowHours = int(datetime.now().strftime("%H"))
    nowMinutes = int(datetime.now().strftime("%M"))
    tm1 = timedelta(hours=nowHours, minutes=nowMinutes)
    tm2 = timedelta(hours=delhours, minutes=delminutes)
    result = str(tm1 + tm2)
    result = result[:-3:] 
    if len(result)>5:
        result = result[7::]
    if len(result) == 4:
        result = '0'+result
    return result
    # print(result)



# функция выбирающая подходящих пользователей по начальной и конечной точке 
def selector_with_start_final(userid):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    spoint = start_getter(userid)
    fpoint = finish_getter(userid)
    cur.execute("SELECT * FROM users WHERE start=? AND finish=? AND userid != ?",
          (spoint, fpoint, userid))
    podhodyshie_users= cur.fetchall()
    return podhodyshie_users





# функция выбирающая юзеров по времени 
def selector_with_timePeriod(fTime, sTime, userid):
    arr_neccesary_time = [] 
    podhodyshie_users = selector_with_start_final(userid)
    if len(podhodyshie_users) == 0:
        return []

    arr_of_suitable_users = []
    for i in range(fTime, sTime):
        arr_neccesary_time.append(i)

    for user in podhodyshie_users:
        fTime_user = user[4]
        sTime_user = user[5]
        for i in range(fTime_user, sTime_user):
            if i in arr_neccesary_time:
                arr_of_suitable_users.append(user)
                break
    return arr_of_suitable_users



# выходим с бота 
if __name__ == '__main__':
    executor.start_polling(dp)