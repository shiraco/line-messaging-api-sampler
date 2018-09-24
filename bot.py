# coding: utf-8

import os
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN', '')
LINE_CHANNEL_SECRET = os.environ.get('LINE_CHANNEL_SECRET', '')

import json

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,
    LineBotApiError
)
from linebot.models import (
    FollowEvent,
    MessageEvent,
    TextMessage, TextSendMessage,
    StickerMessage, StickerSendMessage,
    RichMenu, RichMenuBounds, RichMenuArea, RichMenuSize,
    URIAction
)

app = Flask(__name__)

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world!"

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

@handler.add(FollowEvent)
def handle_follow(event):

    app.logger.debug("event: " + str(event))

    rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=2500, height=1686),
        selected=False,
        name="Nice richmenu",
        chat_bar_text="Tap here",
        areas=[RichMenuArea(bounds=RichMenuBounds(x=0, y=0, width=2500, height=1686),
                            action=URIAction(label='Go to line.me', uri='https://line.me'))]
        )
    rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)

    path = './rich_menu.jpg'
    content_type = 'image/jpeg'
    with open(path, 'rb') as f:
        line_bot_api.set_rich_menu_image(rich_menu_id, content_type, f)

    line_bot_api.link_rich_menu_to_user('all', rich_menu_id)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="follow"))


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    app.logger.debug("event: " + str(event))

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):

    app.logger.debug("event: " + str(event))

    path = './stickers.json'
    with open(path) as f:
        SENDABLE_STICKERS = json.load(f)

    stickers = [(sendables[0], sticker_id) for sendables in SENDABLE_STICKERS for sticker_id in sendables[1]]
    package_id, sticker_id = event.message.package_id, event.message.sticker_id

    app.logger.debug((package_id, sticker_id))

    if (package_id, sticker_id) in stickers:
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(package_id=package_id,
                               sticker_id=sticker_id))

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='not support sticker'))


if __name__ == "__main__":
    app.run()
