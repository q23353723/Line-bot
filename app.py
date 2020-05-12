from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import dbcontroller *
import message *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('54etccBz7LuZ7ht2ju8n+7O3SGbWZBU01eRgTr0SbUSF8FyCw1fxuKBlat6JUHmfuPTria3Fw86WLTAcVg1PFioeGKy8Ed8sG4QjRRKxy9Z8VM77Ng3ASbbgzXGGuWwBs8/ACt+f4Ss17hIpLr7sxQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('d191e77c303a0aa0cbe07cca8eab67a9')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)


    if event.message.text == "吉娃娃":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "老子是地表最會睡吉娃娃"))
    if event.message.text == "學詞語":
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text = 'index', contents = learnMenu())

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
