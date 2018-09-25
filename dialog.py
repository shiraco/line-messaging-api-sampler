# coding: utf-8

from linebot.models import (
    TextSendMessage, TemplateSendMessage,
    ButtonsTemplate, ConfirmTemplate,
    ImageCarouselTemplate, ImageCarouselColumn,
    CarouselTemplate, CarouselColumn,
    PostbackAction, MessageAction, URIAction
)

class Dialog(object):

    def __init__(self):
        self.user_context = None

    def dialog(self, message, user_id):

        received_message = message.text
        sending_message = self.think(received_message)

        return sending_message

    def think(self, received_message):
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

        else:
            sending_message = TextSendMessage(received_message)

        return sending_message
