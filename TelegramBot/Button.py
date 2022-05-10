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
        text="2. 학사일정", callback_data="2")
    btn_key3 = InlineKeyboardButton(
        text="3. 학사", callback_data="3")
    mu = InlineKeyboardMarkup(inline_keyboard=[[btn_key, btn_key2, btn_key3]])
    bot.sendMessage(chat_id, "선택하세요", reply_markup=mu)


def query_ans(msg):
    query_id = msg["id"]
    query_data = msg["data"]
    if query_data == "1":
        bot.sendMessage(chat_id, text="경기도 용인시 처인구 모현읍 외대로 81 (왕산리)")
    elif query_data == "2":
        bot.sendMessage(chat_id, text="학사일정")


bot.sendMessage(chat_id, "hihihi")

MessageLoop(
    bot, {'chat': btn_show, 'callback_query': query_ans}).run_as_thread()

while True:
    time.sleep(5)
