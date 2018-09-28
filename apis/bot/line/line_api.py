# coding: utf-8

from linebot import (
    LineBotApi
)

class LineBotLinkApi(LineBotApi):
    def link_account(self, user_id, timeout=None):
        """Call link account to user API.
        https://developers.line.me/ja/reference/messaging-api/#issue-link-token
        :param str user_id: user id
        :type timeout: float | tuple(float, float)
        :return: linkToken
        """
        response = self._post(
            '/v2/bot/user/{user_id}/linkToken'.format(
                user_id=user_id
            ),
            timeout=timeout
        )
        return response.json.get('linkToken')

    def unlink_account(self, user_id, timeout=None):
        """Call unlink account from user API.
        https://developers.line.me/en/docs/messaging-api/reference/#unlink-rich-menu-from-user
        :param str user_id: ID of the user
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._delete(
            '/v2/bot/user/{user_id}/richmenu'.format(user_id=user_id),
            timeout=timeout
        )
