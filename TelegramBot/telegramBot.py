import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# token = "5382062842:AAFy953rQtlu2l6M0DIpzQCdJXJrWAJemU4"
# bot = telegram.Bot(token="5382062842:AAFy953rQtlu2l6M0DIpzQCdJXJrWAJemU4")

chat_id = 5081938343


with open("token.txt") as f:
    lines = f.readlines()
    token = lines[0].strip()

# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


# command hander
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# polling
updater.start_polling()

bot.sendMessage(chat_id=chat_id,
                text="경기도 용인시 처인구 모현읍 외대로 81 (왕산리)")  # 메세지 보내기


'''def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def get_command(update, context):
    print("get")
    show_list = []
    show_list.append(InlineKeyboardButton(
        "학교위치", callback_data="경기도 용인시 처인구 모현읍 외대로 81 (왕산리)"))  # add on button
    show_list.append(InlineKeyboardButton(
        "학사정보", callback_data="학사정보"))  # add off button
    show_list.append(InlineKeyboardButton(
        "cancel", callback_data="cancel"))  # add cancel button
    show_markup = InlineKeyboardMarkup(build_menu(
        show_list, len(show_list) - 1))  # make markup

    update.message.reply_text("원하는 값을 선택하세요", reply_markup=show_markup)


btn_key = InlineKeyboardButton(
    text="1. 학교위치", callback_data="1")
btn_key2 = InlineKeyboardButton(
    text="2. 학사일정", callback_data="2")


def btn_show(msg):
    input_chat = msg['text']
    btn_key = InlineKeyboardButton(
        text="1. 학교위치", callback_data="1")
    btn_key2 = InlineKeyboardButton(
        text="2. 학사일정", callback_data="2")
    mu = InlineKeyboardMarkup(inline_keyboard=[[btn_key, btn_key2]])
    bot.sendMessage(chat_id, "선택하세요", reply_markup=mu)


def query_ans(msg):
    query_id = msg["id"]
    query_data = msg["data"]
    if query_data == "1":
        bot.sendMessage(query_id, text="경기도 용인시 처인구 모현읍 외대로 81 (왕산리)")
    elif query_data == "2":
        bot.answerCallbackQuery(query_id, text="학사일정")
'''
