import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
my_token = ""
bot = telegram.Bot(token="")
chat_id = 5081938343


updater = Updater(my_token, use_context=True)


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
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


get_handler = CommandHandler('get', get_command)
updater.dispatcher.add_handler(get_handler)

updater.start_polling(timeout=1, clean=True)
updater.idle()


'''btn_key = InlineKeyboardButton(
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


MessageLoop(
    bot, {'chat': btn_show, 'callback_query': query_ans}).run_as_thread()

'''
'''bot.sendMessage(chat_id=chat_id,
                text="경기도 용인시 처인구 모현읍 외대로 81 (왕산리)")  # 메세지 보내기'''
