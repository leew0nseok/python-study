import telepot
import time
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup
from telepot.namedtuple import InlineKeyboardButton

token = "5382062842:AAFy953rQtlu2l6M0DIpzQCdJXJrWAJemU4"
bot = telepot.Bot(token)

chat_id = '5081938343'


# 메세지 처리 함수


def btn_show(msg):
    input_chat = msg['text']
    btn_key = InlineKeyboardButton(
        text="1. 학교위치", callback_data="1")
    btn_key2 = InlineKeyboardButton(
        text="2. 학사", callback_data="2")
    btn_key3 = InlineKeyboardButton(
        text="3. 수업", callback_data="3")
    btn_key4 = InlineKeyboardButton(
        text="4. 전공", callback_data="4")
    mu = InlineKeyboardMarkup(
        inline_keyboard=[[btn_key, btn_key2, btn_key3], [btn_key4]])
    bot.sendMessage(chat_id, "선택하세요", reply_markup=mu)


def query_ans(msg):
    query_id = msg["id"]
    query_data = msg["data"]
    if query_data == "1":
        bot.sendMessage(chat_id, text="학교위치를 선택하셨습니다.")
        bot.sendMessage(chat_id, text="경기도 용인시 처인구 모현읍 외대로 81 (왕산리)")
    elif query_data == "2":
        btn_key = InlineKeyboardButton(
            text="1. 학사일정", callback_data="학사일정")
        btn_key2 = InlineKeyboardButton(
            text="2. 학사안내", callback_data="학사안내")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2]])
        bot.sendMessage(chat_id, "학사를 선택하셨습니다.", reply_markup=mu)
    elif query_data == "3":
        btn_key = InlineKeyboardButton(
            text="1. 수강신청", callback_data="수강신청")
        btn_key2 = InlineKeyboardButton(
            text="2. 계절학기", callback_data="계절학기")
        btn_key3 = InlineKeyboardButton(
            text="3. 성적", callback_data="성적")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2, btn_key3]])
        bot.sendMessage(chat_id, "수업을 선택하셨습니다.", reply_markup=mu)
    elif query_data == "학사일정":
        bot.sendMessage(chat_id, text="학사일정을 선택하셨습니다.")
        f = open('C:\\Users\\LEE\\Desktop\\StudyPython\\Datas\\학사일정.PNG', 'rb')
        bot.sendPhoto(chat_id, f)
    elif query_data == "수강신청":
        bot.sendMessage(chat_id, text="수강신청을 선택하셨습니다.")
    elif query_data == "계절학기":
        bot.sendMessage(chat_id, text="계절학기를 선택하셨습니다.")
    elif query_data == "성적":
        bot.sendMessage(chat_id, text="성적을 선택하셨습니다.")
        f = open('C:\\Users\\LEE\\Desktop\\StudyPython\\Datas\\성적.PNG', 'rb')
        bot.sendPhoto(chat_id, f)


bot.sendMessage(chat_id, "hihihi")

MessageLoop(
    bot, {'chat': btn_show, 'callback_query': query_ans}).run_as_thread()

while True:
    time.sleep(5)
