# -*- coding:utf-8 -*-
from teelebot import Bot
from threading import Timer

bot = Bot()

def About(message):
    chat_id = message["chat"]["id"]
    message_id = message["message_id"]
    text = message["text"]
    prefix = "about"

    with open(bot.plugin_dir + "About/config.ini", 'r', encoding="utf-8") as g:
        first_btn = g.readline().strip().split(',')
        last_btn = g.readline().strip().split(',')

    if text[1:len(prefix)+1] == prefix:
        inlineKeyboard = [
            [
                {"text": first_btn[0], "url": first_btn[1]},
                {"text": last_btn[0], "url": last_btn[1]},
            ]
        ]
        reply_markup = {
            "inline_keyboard": inlineKeyboard
        }
        status = bot.sendChatAction(chat_id, "typing")
        msg = "此Bot基于 <b>teelebot</b> 框架 <b>v" + bot.VERSION + "</b>%0A%0A" +\
            "<b>teelebot</b> 是基于Telegram Bot API 的 Bot 框架，具有插件系统，扩展方便。%0A%0A"

        req = bot.getUserProfilePhotos(user_id=str(bot.getMe()["id"]), limit=1)
        bot_icon = req.get("photos")[0][0]["file_id"]
        if type(bot_icon) == str and len(bot_icon) > 50:
            photo = bot_icon
        else:
            with open(bot.plugin_dir + "About/icon.png", "rb") as p:
                photo = p.read()

        status = bot.sendPhoto(chat_id=chat_id, photo=photo, caption=msg, parse_mode="HTML", reply_to_message_id=message_id, reply_markup=reply_markup)
        timer = Timer(60, timer_func, args=[chat_id, status["message_id"]])
        timer.start()
    else:
        status = bot.sendChatAction(chat_id, "typing")
        status = bot.sendMessage(chat_id=chat_id, text="指令格式错误，请检查!", parse_mode="HTML", reply_to_message_id=message_id)
        timer = Timer(15, timer_func, args=[chat_id, status["message_id"]])
        timer.start()




def timer_func(chat_id, message_id):
    status = bot.deleteMessage(chat_id=chat_id, message_id=message_id)