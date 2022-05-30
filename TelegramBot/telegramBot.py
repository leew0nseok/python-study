import telepot
import time
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup
from telepot.namedtuple import InlineKeyboardButton
import pdfcapture

token = "5382062842:AAFy953rQtlu2l6M0DIpzQCdJXJrWAJemU4"
bot = telepot.Bot(token)

chat_id = '5081938343'

# 메세지 처리 함수


def btn_show(msg):
    input_chat = msg['text']
    btn_key = InlineKeyboardButton(
        text="1. 학교", callback_data="학교")
    btn_key2 = InlineKeyboardButton(
        text="2. 학사일정", callback_data="학사일정")
    btn_key3 = InlineKeyboardButton(
        text="3. 수업", callback_data="수업")
    btn_key4 = InlineKeyboardButton(
        text="4. 전공관련", callback_data="전공관련")
    btn_key5 = InlineKeyboardButton(
        text="5. 성적", callback_data="성적")
    btn_key6 = InlineKeyboardButton(
        text="6. 이수학점", callback_data="이수학점")
    btn_key7 = InlineKeyboardButton(
        text="7. English Zone", callback_data="English Zone")
    btn_key8 = InlineKeyboardButton(
        text="8. Coding Zone", callback_data="Coding Zone")
    btn_key9 = InlineKeyboardButton(
        text="9. 교통안내", callback_data="교통안내")
    btn_key10 = InlineKeyboardButton(
        text="10. 학교관련 앱", callback_data="학교관련 앱")

    mu = InlineKeyboardMarkup(
        inline_keyboard=[[btn_key, btn_key2, btn_key3, btn_key4], [btn_key5, btn_key6, btn_key7, btn_key8], [btn_key9, btn_key10]])
    bot.sendMessage(chat_id, "원하는 정보를 선택하세요.", reply_markup=mu)


def query_ans(msg):
    query_id = msg["id"]
    query_data = msg["data"]
    # 1.
    if query_data == "학교":
        btn_key = InlineKeyboardButton(
            text="1. 학교위치", callback_data="학교위치")
        btn_key2 = InlineKeyboardButton(
            text="2. 강의실 안내", callback_data="강의실")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2]])
        bot.sendMessage(chat_id, "학교를 선택하셨습니다.", reply_markup=mu)
    elif query_data == "학교위치":
        bot.sendMessage(chat_id, text="경기도 용인시 처인구 모현읍 외대로 81 (왕산리)")
    elif query_data == "강의실":
        sendcapture(5, "강의실")

    # 2.
    elif query_data == "학사일정":
        sendcapture(4, "학사일정")

    # 3.
    elif query_data == "수업":
        btn_key = InlineKeyboardButton(
            text="1. 수강신청", callback_data="수강신청")
        btn_key2 = InlineKeyboardButton(
            text="2. 학기당 최대 수강학점", callback_data="수강학점")
        btn_key3 = InlineKeyboardButton(
            text="3. 수강신청 유의사항", callback_data="유의사항")
        btn_key4 = InlineKeyboardButton(
            text="4. 수업시간", callback_data="수업시간")
        btn_key5 = InlineKeyboardButton(
            text="5. 재수강", callback_data="재수강")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2], [btn_key3, btn_key4, btn_key5]])
        bot.sendMessage(chat_id, "수업을 선택하셨습니다.", reply_markup=mu)
    elif query_data == "수강신청":
        sendcapture(5, "수강신청")
    elif query_data == "수강학점":
        sendcapture(5, "수강학점")
    elif query_data == "유의사항":
        sendcapture(5, "유의사항")
    elif query_data == "수업시간":
        sendcapture(5, "수업시간")
    elif query_data == "재수강":
        sendcapture(10, "7.  재수강")

    # 4.
    elif query_data == "전공관련":
        btn_key = InlineKeyboardButton(
            text="1. 전공", callback_data="전공")
        btn_key2 = InlineKeyboardButton(
            text="2. 이중전공, 부전공", callback_data="이중전공")
        btn_key3 = InlineKeyboardButton(
            text="3. 후기이중전공", callback_data="후기이중전공")
        btn_key4 = InlineKeyboardButton(
            text="4. 융합전공", callback_data="융합전공")
        btn_key5 = InlineKeyboardButton(
            text="5. 전과", callback_data="전과")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2], [btn_key3, btn_key4, btn_key5]])
        bot.sendMessage(chat_id, "전공을 선택하셨습니다.", reply_markup=mu)
    elif query_data == "전공":
        sendcapture(9, "전공")
    elif query_data == "이중전공":
        sendcapture(9, "이중전공  및  전공심화")
    elif query_data == "후기이중전공":
        sendcapture(10, "5.  후기이중전공")
    elif query_data == "융합전공":
        sendcapture(10, "6.  융합전공")
    elif query_data == "전과":
        sendcapture(11, "전과")

    # 5.
    elif query_data == "성적":
        btn_key = InlineKeyboardButton(
            text="1. 성적평가유형", callback_data="성적평가")  # 수강편람에 없는 자료(따로 구해서 보내야함)
        btn_key2 = InlineKeyboardButton(
            text="2. 학점", callback_data="학점")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2]])
        bot.sendMessage(chat_id, "성적을 선택하셨습니다.", reply_markup=mu)
    elif query_data == "성적평가":
        f = open('', 'rb')
        bot.sendPhoto(chat_id, f)
    elif query_data == "학점":
        f = open('C:\\Users\\LEE\\Desktop\\StudyPython\\Datas\\성적.PNG', 'rb')
        bot.sendPhoto(chat_id, f)

    # 6.
    elif query_data == "이수학점":
        btn_key = InlineKeyboardButton(
            text="1. 졸업필요 이수학점", callback_data="졸업학점")
        btn_key2 = InlineKeyboardButton(
            text="2. 교양 교과목", callback_data="교양")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2]])
        bot.sendMessage(chat_id, "졸업관련 항목을 선택하셨습니다.", reply_markup=mu)
    elif query_data == "졸업학점":
        sendcapture(6, "이수학점")
    elif query_data == "교양":
        sendcapture(7, "교양")  # 이미지가 더 보내짐

    elif query_data == "English Zone":
        bot.sendMessage(chat_id, "English Zone을 선택하셨습니다.")

    elif query_data == "Coding Zone":
        bot.sendMessage(chat_id, "Coding Zone을 선택하셨습니다.")

    # 9.
    elif query_data == "교통안내":
        btn_key = InlineKeyboardButton(
            text="1. 대중교통", callback_data="대중교통")
        btn_key2 = InlineKeyboardButton(
            text="2. 학생통학버스", callback_data="학생통학버스")
        btn_key3 = InlineKeyboardButton(
            text="3. 교내 셔틀버스", callback_data="교내 셔틀")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2, btn_key3]])
        bot.sendMessage(chat_id, "학생통학버스를 선택하셨습니다.", reply_markup=mu)
    elif query_data == "대중교통":
        sendcapture(30, "대중교통")
    elif query_data == "학생통학버스":
        sendcapture(31, "")
        sendcapture(32, "")  # 전체페이지 출력안되고 위에가 짤림
    elif query_data == "교내 셔틀":
        sendcapture(33, "셔틀버스")

    elif query_data == "학교관련 앱":
        btn_key = InlineKeyboardButton(
            text="1. 한국외대 앱", callback_data="한국외대 앱")
        btn_key2 = InlineKeyboardButton(
            text="2. 한국외대 모바일ID", callback_data="한국외대 모바일ID")
        mu = InlineKeyboardMarkup(
            inline_keyboard=[[btn_key, btn_key2]])
        bot.sendMessage(chat_id, "졸업관련 항목을 선택하셨습니다.", reply_markup=mu)
    elif query_data == "한국외대 앱":
        bot.sendMessage(
            chat_id, "구글 Android: https://play.google.com/store/apps/details?id=kr.ac.hufs.mobilecampus&hl=ko&gl=US")
        bot.sendMessage(
            chat_id, "아이폰(ios): https://apps.apple.com/kr/app/%ED%95%9C%EA%B5%AD%EC%99%B8%EB%8C%80/id1032310471")
    elif query_data == "한국외대 모바일ID":
        bot.sendMessage(
            chat_id, "구글 Android: https://play.google.com/store/apps/details?id=com.nexmotion.hufs&hl=ko&gl=US")
        bot.sendMessage(
            chat_id, "아이폰(ios): https://apps.apple.com/kr/app/%ED%95%9C%EA%B5%AD%EC%99%B8%EA%B5%AD%EC%96%B4%EB%8C%80%ED%95%99%EA%B5%90-%EB%AA%A8%EB%B0%94%EC%9D%BCid/id1503615753")


def sendcapture(num, msg=None):  # pdfcapture모듈에서 이미지 저장 후 파일 보내기
    pdfcapture.capture_img(num, msg)
    f = open('sendimgfile.jpg', 'rb')
    bot.sendPhoto(chat_id, f)


bot.sendMessage(chat_id, "아무키나 입력하세요.")

MessageLoop(
    bot, {'chat': btn_show, 'callback_query': query_ans}).run_as_thread()

while True:
    time.sleep(5)
