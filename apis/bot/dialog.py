# coding: utf-8

from linebot.models import (
    TextSendMessage, TemplateSendMessage,
    ButtonsTemplate, ConfirmTemplate,
    ImageCarouselTemplate, ImageCarouselColumn,
    CarouselTemplate, CarouselColumn,
    PostbackAction, MessageAction, URIAction,
    QuickReply, QuickReplyButton,
    FlexSendMessage, BubbleContainer,
    BoxComponent, ImageComponent, TextComponent,
    BubbleStyle, BlockStyle
)

import os
PROVIDER_URL = os.environ.get('PROVIDER_URL', '')

class Dialog(object):

    def __init__(self, line_bot_api):
        self.user_context = None
        self.line_bot_api = line_bot_api

    def dialog(self, message, user_id):

        received_message = message.text

        linkToken = None
        if 'ログイン' in received_message:
            linkToken = self.line_bot_api.link_account(user_id)

        sending_message = self.think_reply_message(received_message, option=linkToken)

        return sending_message

    def think_reply_message(self, received_message, option=None):
        if 'ボタンテンプレート' in received_message:
            sending_message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://placehold.jp/565656/151x100.png',
                    title='Menu',
                    text='Please select',
                    actions=[
                        PostbackAction(
                            label='postback',
                            text='postback text',
                            data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message',
                            text='message text'
                        ),
                        URIAction(
                            label='uri',
                            uri='http://example.com/'
                        )
                    ]
                )
            )

        elif '確認テンプレート' in received_message:
            sending_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='Are you sure?',
                    actions=[
                        PostbackAction(
                            label='postback',
                            text='postback text',
                            data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message',
                            text='message text'
                        )
                    ]
                )
            )

        elif '画像カルーセルテンプレート' in received_message:
            sending_message = TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://placehold.jp/ababab/150x150.png',
                            action=PostbackAction(
                                label='postback1',
                                text='postback text1',
                                data='action=buy&itemid=1'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://placehold.jp/565656/150x150.png',
                            action=PostbackAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            )
                        )
                    ]
                )
            )

        elif 'カルーセルテンプレート' in received_message:
            sending_message = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url='https://placehold.jp/ababab/100x151.png',
                            title='this is menu1',
                            text='description1',
                            actions=[
                                PostbackAction(
                                    label='postback1',
                                    text='postback text1',
                                    data='action=buy&itemid=1'
                                ),
                                MessageAction(
                                    label='message1',
                                    text='message text1'
                                ),
                                URIAction(
                                    label='uri1',
                                    uri='http://example.com/1'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://placehold.jp/565656/100x151.png',
                            title='this is menu2',
                            text='description2',
                            actions=[
                                PostbackAction(
                                    label='postback2',
                                    text='postback text2',
                                    data='action=buy&itemid=2'
                                ),
                                MessageAction(
                                    label='message2',
                                    text='message text2'
                                ),
                                URIAction(
                                    label='uri2',
                                    uri='http://example.com/2'
                                )
                            ]
                        )
                    ]
                )
            )

        elif 'フレックス' in received_message:
            sending_message = FlexSendMessage(
                alt_text='ImageCarousel template',
                contents=BubbleContainer(
                    header=BoxComponent(
                        layout='vertical',
                        contents=[
                            TextComponent(
                                text='header'
                            )
                        ]
                    ),
                    hero=ImageComponent(
                        url='https://placehold.jp/ababab/1024x1024.png',
                        size='full'
                    ),
                    body=BoxComponent(
                        layout='vertical',
                        contents=[
                            TextComponent(
                                text='body'
                            )
                        ]
                    ),
                    footer=BoxComponent(
                        layout='vertical',
                        contents=[
                            TextComponent(
                                text='footer'
                            )
                        ]
                    ),
                    styles=BubbleStyle(
                        header=BlockStyle(),
                        hero=BlockStyle(),
                        body=BlockStyle(),
                        footer=BlockStyle()
                    )
                )

            )


        elif 'ログイン' in received_message:
            url = "{provider_url}/link_account?linkToken={link_token}".format(provider_url=PROVIDER_URL, link_token=option)
            sending_message = TemplateSendMessage(
                alt_text='Account Link',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://placehold.jp/565656/100x151.png',
                    title='Menu',
                    text='Link your account',
                    actions=[
                        URIAction(
                            label='Account Link',
                            uri=url
                        )
                    ]
                )
            )

        elif 'ログアウト' in received_message:
            pass

        elif 'クイックリプライ' in received_message:
            sending_message = TextSendMessage(text='Hello, world',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="label01", text="text01"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=01"),
                                   QuickReplyButton(action=MessageAction(label="label02", text="text02"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=02"),
                                   QuickReplyButton(action=MessageAction(label="label03", text="text03"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=03"),
                                   QuickReplyButton(action=MessageAction(label="label04", text="text04"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=04"),
                                   QuickReplyButton(action=MessageAction(label="label05", text="text05"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=05"),
                                   QuickReplyButton(action=MessageAction(label="label06", text="text06"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=06"),
                                   QuickReplyButton(action=MessageAction(label="label07", text="text07"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=07"),
                                   QuickReplyButton(action=MessageAction(label="label08", text="text08"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=08"),
                                   QuickReplyButton(action=MessageAction(label="label09", text="text09"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=09"),
                                   QuickReplyButton(action=MessageAction(label="label10", text="text10"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=10"),
                                   QuickReplyButton(action=MessageAction(label="label11", text="text11"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=11"),
                                   QuickReplyButton(action=MessageAction(label="label12", text="text12"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=12"),
                                   QuickReplyButton(action=MessageAction(label="label13", text="text13"), image_url="https://placehold.jp/24/ffffff/000000/50x50.png?text=13")
                                   ]))
        else:
            sending_message = TextSendMessage(received_message)

        return sending_message
