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
        text="1. 학교", callback_data="학교")
    btn_key2 = InlineKeyboardButton(
        text="2. 학사", callback_data="학사")
    btn_key3 = InlineKeyboardButton(
        text="3. 수업", callback_data="수업")
    btn_key4 = InlineKeyboardButton(
        text="4. 전공", callback_data="전공")
    btn_key5 = InlineKeyboardButton(
        text="5. 성적", callback_data="성적")
    btn_key6 = InlineKeyboardButton(
        text="6. 졸업관련", callback_data="졸업관련")
    btn_key7 = InlineKeyboardButton(
        text="7. English Zone", callback_data="English Zone")
    btn_key8 = InlineKeyboardButton(
        text="8. Coding Zone", callback_data="Coding Zone")
    mu = InlineKeyboardMarkup(
        inline_keyboard=[[btn_key, btn_key2, btn_key3, btn_key4], [btn_key5, btn_key6, btn_key7, btn_key8]])
    bot.sendMessage(chat_id, "궁금하신 것을 선택하세요", reply_markup=mu)


def query_ans(msg):
    query_id = msg["id"]
    query_data = msg["data"]
    if query_data == "학교":
        btn_key = InlineKeyboardButton(
            text="1. 학교위치", callback_data="학교위치")
        btn_key2 = InlineKeyboardButton(
            text="2. 건물위치, 번호", callback_data="건물")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2]])
        bot.sendMessage(chat_id, "학교를 선택하셨습니다.", reply_markup=mu)

    elif query_data == "학사":
        btn_key = InlineKeyboardButton(
            text="1. 학사일정", callback_data="학사일정")
        btn_key2 = InlineKeyboardButton(
            text="2. 학사안내", callback_data="학사안내")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2]])
        bot.sendMessage(chat_id, "학사를 선택하셨습니다.", reply_markup=mu)

    elif query_data == "수업":
        btn_key = InlineKeyboardButton(
            text="1. 수강신청", callback_data="수강신청")
        btn_key2 = InlineKeyboardButton(
            text="2. 계절학기", callback_data="계절학기")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2]])
        bot.sendMessage(chat_id, "수업을 선택하셨습니다.", reply_markup=mu)

    elif query_data == "전공":
        btn_key = InlineKeyboardButton(
            text="1. 전공심화", callback_data="전공심화")
        btn_key2 = InlineKeyboardButton(
            text="2. 아중전공, 부전공", callback_data="이중")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2]])
        bot.sendMessage(chat_id, "전공을 선택하셨습니다.", reply_markup=mu)

    elif query_data == "성적":
        btn_key = InlineKeyboardButton(
            text="1. 성적평가유형", callback_data="성적평가")
        btn_key2 = InlineKeyboardButton(
            text="2. 학점", callback_data="학점")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2]])
        bot.sendMessage(chat_id, "성적을 선택하셨습니다.", reply_markup=mu)

    elif query_data == "졸업관련":
        btn_key = InlineKeyboardButton(
            text="1. 졸업 이수학점", callback_data="졸업학점")
        btn_key2 = InlineKeyboardButton(
            text="2. 필수과목", callback_data="필수과목")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2]])
        bot.sendMessage(chat_id, "졸업관련 항목을 선택하셨습니다.", reply_markup=mu)

    elif query_data == "English Zone":
        bot.sendMessage(chat_id, "English Zone을 선택하셨습니다.")

    elif query_data == "Coding Zone":
        bot.sendMessage(chat_id, "Coding Zone을 선택하셨습니다.")

    elif query_data == "학교위치":
        bot.sendMessage(chat_id, text="학교위치를 선택하셨습니다.")
        bot.sendMessage(chat_id, text="경기도 용인시 처인구 모현읍 외대로 81 (왕산리)")

    elif query_data == "학사일정":
        bot.sendMessage(chat_id, text="학사일정을 선택하셨습니다.")
        f = open('C:\\Users\\LEE\\Desktop\\StudyPython\\Datas\\학사일정.PNG', 'rb')
        bot.sendPhoto(chat_id, f)

    elif query_data == "수강신청":
        bot.sendMessage(chat_id, text="수강신청을 선택하셨습니다.")

    elif query_data == "계절학기":
        bot.sendMessage(chat_id, text="계절학기를 선택하셨습니다.")

    elif query_data == "학점":
        bot.sendMessage(chat_id, text="학점을 선택하셨습니다.")
        f = open('C:\\Users\\LEE\\Desktop\\StudyPython\\Datas\\성적.PNG', 'rb')
        bot.sendPhoto(chat_id, f)


bot.sendMessage(chat_id, "아무키나 입력하세요.")

MessageLoop(
    bot, {'chat': btn_show, 'callback_query': query_ans}).run_as_thread()

while True:
    time.sleep(5)
