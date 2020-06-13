# -*- coding:utf-8 -*-
import requests
from teelebot import Bot
import urllib.parse as ubp

def Chat(message):
    bot = Bot()
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg="
    requests.adapters.DEFAULT_RETRIES = 5
    hello = ("你好", "nihao", "hello", "Hello",
            "HELLO", "hi", "Hi", "HI",
             "早上好", "上午好", "下午好", "晚上好", "中午好",
             "good morning", "Good morning", "good afternoom",
             "Good afternoom", "good evening", "Good evening")
    if message["text"][1:] in hello:
        status = bot.sendChatAction(message["chat"]["id"], "typing")
        status = bot.sendVoice(message["chat"]["id"], voice=bot.plugin_dir + "Chat/hello.ogg", reply_to_message_id=message["message_id"])
    else:
        with requests.get(url + ubp.quote(message["text"][1:])) as req: #urlencode编码
            req.keep_alive = False
            req.encoding = "utf-8"
            status = bot.sendChatAction(message["chat"]["id"], "typing")
            status = bot.sendMessage(message["chat"]["id"], str(req.json().get("content").replace("{br}", "%0A").replace("菲菲", "小埋")), parse_mode="HTML", reply_to_message_id=message["message_id"])