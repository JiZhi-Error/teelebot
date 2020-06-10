# -*- coding:utf-8 -*-
from teelebot import Bot
from teelebot.handler import config
from threading import Timer

bot = Bot()
bot_id = str(bot.getMe()["id"])
config = config()

def ID(message):
    if "reply_to_message" not in message.keys():
        status = bot.sendChatAction(message["chat"]["id"], "typing")
        if str(message["from"]["id"]) == config["root"]:
            status = bot.sendChatAction(message["chat"]["id"], "typing")
            status = bot.sendMessage(message["chat"]["id"], "主人，" + "您的用户ID为：<b>" + str(message["from"]["id"]) + "</b>", parse_mode="HTML", reply_to_message_id=message["message_id"])
        else:
            status = bot.sendChatAction(message["chat"]["id"], "typing")
            status = bot.sendMessage(message["chat"]["id"], str(message["from"]["first_name"]) + "%0A您的用户ID为：<b>" + str(message["from"]["id"]) + "</b>", parse_mode="HTML", reply_to_message_id=message["message_id"])
        timer = Timer(30, timer_func_for_del, args=[status["chat"]["id"], status["message_id"]])
        timer.start()
    elif "reply_to_message" in message.keys() and message["chat"]["type"] != "private":
        admins = administrators(message["chat"]["id"])

        if message["chat"]["type"] != "private":
            admins = administrators(chat_id=message["chat"]["id"])
            if str(config["root"]) not in admins:
                admins.append(str(config["root"])) #root permission

        if str(message["from"]["id"]) in admins:
            reply_to_message = message["reply_to_message"]
            target_message_id = reply_to_message["message_id"]
            target_user_id = reply_to_message["from"]["id"]
            target_chat_id = reply_to_message["chat"]["id"]

            if str(bot_id) != str(target_user_id):
                if str(message["from"]["id"]) == config["root"]:
                    status = bot.sendChatAction(message["chat"]["id"], "typing")
                    status = bot.sendMessage(message["chat"]["id"], "主人，您查询的用户的ID为：<b>" + str(target_user_id) + "</b>", parse_mode="HTML", reply_to_message_id=message["message_id"])
                else:
                    status = bot.sendChatAction(message["chat"]["id"], "typing")
                    status = bot.sendMessage(message["chat"]["id"], str(message["from"]["first_name"]) + ",您查询的用户的ID为：<b>" + str(target_user_id) + "</b>", parse_mode="HTML", reply_to_message_id=message["message_id"])
                timer = Timer(30, timer_func_for_del, args=[status["chat"]["id"], status["message_id"]])
                timer.start()
            else:
                if str(message["from"]["id"]) == config["root"]:
                    status = bot.sendChatAction(message["chat"]["id"], "typing")
                    status = bot.sendMessage(message["chat"]["id"], "主人，我的ID为：<b>" + str(target_user_id) + "</b>", parse_mode="HTML", reply_to_message_id=message["message_id"])
                else:
                    status = bot.sendChatAction(message["chat"]["id"], "typing")
                    status = bot.sendMessage(chat_id=message["chat"]["id"], text="抱歉，您无权查询!", parse_mode="text", reply_to_message_id=message["message_id"])
                timer = Timer(30, timer_func_for_del, args=[status["chat"]["id"], status["message_id"]])
                timer.start()
        else:
            status = bot.sendChatAction(message["chat"]["id"], "typing")
            status = bot.sendMessage(chat_id=message["chat"]["id"], text="抱歉，您无权查询!", parse_mode="text", reply_to_message_id=message["message_id"])
            timer = Timer(30, timer_func_for_del, args=[status["chat"]["id"], status["message_id"]])
            timer.start()
    elif "reply_to_message" in message.keys() and message["chat"]["type"] == "private":
        reply_to_message = message["reply_to_message"]
        target_message_id = reply_to_message["message_id"]
        target_user_id = reply_to_message["from"]["id"]
        target_chat_id = reply_to_message["chat"]["id"]

        if str(bot_id) == str(target_user_id):
            if str(message["from"]["id"]) == config["root"]:
                status = bot.sendChatAction(message["chat"]["id"], "typing")
                status = bot.sendMessage(message["chat"]["id"], "主人，我的ID为：<b>" + str(target_user_id) + "</b>", parse_mode="HTML", reply_to_message_id=message["message_id"])
            else:
                status = bot.sendChatAction(message["chat"]["id"], "typing")
                status = bot.sendMessage(chat_id=message["chat"]["id"], text="抱歉，您无权查询!", parse_mode="text", reply_to_message_id=message["message_id"])
            timer = Timer(30, timer_func_for_del, args=[status["chat"]["id"], status["message_id"]])
            timer.start()
        else:
            if str(message["from"]["id"]) == config["root"]:
                status = bot.sendChatAction(message["chat"]["id"], "typing")
                status = bot.sendMessage(message["chat"]["id"], "主人，您查询的用户的ID为：<b>" + str(target_user_id) + "</b>", parse_mode="HTML", reply_to_message_id=message["message_id"])
            elif message["chat"]["id"] == target_user_id:
                status = bot.sendChatAction(message["chat"]["id"], "typing")
                status = bot.sendMessage(message["chat"]["id"], str(message["from"]["first_name"]) + ",您的用户ID为：<b>" + str(target_user_id) + "</b>", parse_mode="HTML", reply_to_message_id=message["message_id"])
            timer = Timer(30, timer_func_for_del, args=[status["chat"]["id"], status["message_id"]])
            timer.start()

def administrators(chat_id):
    admins = []
    results = bot.getChatAdministrators(chat_id=chat_id)
    if results != False:
        for result in results:
            if str(result["user"]["is_bot"]) == "False":
                admins.append(str(result["user"]["id"]))
    else:
        admins = False

    return admins


def timer_func_for_del(chat_id, message_id):
    status = bot.deleteMessage(chat_id=chat_id, message_id=message_id)