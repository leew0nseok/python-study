
# 모듈설정
import telegram
import telepot  # pip install telepot
import psutil
import os
from telepot.loop import MessageLoop  # 봇구동
from telepot.namedtuple import InlineKeyboardMarkup as MU  # 마크업
from telepot.namedtuple import InlineKeyboardButton as BT  # 버튼
import time
import sys

# 알림받을 텔레그램 사용자 정보 입력
token = "5382062842:AAFy953rQtlu2l6M0DIpzQCdJXJrWAJemU4"
mc = '5081938343'
bot = telepot.Bot(token)


# IP 버튼 생성

def btn_show(msg):
    btn1 = BT(text="1.1.1.1", callback_data="1")
    btn2 = BT(text="1.1.1.1", callback_data="2")

    # IP 버튼 가로 정렬
    mu = MU(inline_keyboard=[[btn1, btn2]])

    # 1차 응답 (버튼제목)
    bot.sendMessage(mc, " ☞  모니터링할 IP를 선택하세요 ", reply_markup=mu)

# 콜백 받은 대답 처리


def query_ans(msg):
    query_data = msg["data"]
    f = open('../data.txt')
    if query_data == "1":
        lines = f.readline()
        bot.sendMessage(mc, "▷ Memory Usage : "+lines.split(',')[1]+"\n" + "▷ Disk Usage : "+lines.split(
            ',')[2]+"\n" + "▷ Cpu Load : "+lines.split(',')[3].rstrip('\n'))
    elif query_data == "2":
        lines = f.readline()
        lines = f.readline()
        bot.sendMessage(mc, "▷ Memory Usage : "+lines.split(',')[1]+"\n" + "▷ Disk Usage : "+lines.split(
            ',')[2]+"\n" + "▷ Cpu Load : "+lines.split(',')[3].rstrip('\n'))


MessageLoop(
    bot, {'chat': btn_show, 'callback_query': query_ans}). run_as_thread()

# 코드가 참일 경우 프로세스 계속 유지
while True:
    time.sleep(5)
