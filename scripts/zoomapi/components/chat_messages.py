"""Zoom.us REST API Python Client -- Chat Messages component"""

from zoomapi.util import require_keys, Throttled
from zoomapi.components import base
import requests


class ChatMessagesComponentV2(base.BaseComponent):
    """Component dealing with all chat messages related matters"""

    @Throttled
    def list(self, **kwargs) -> requests.Response:
        """
        https://marketplace.zoom.us/docs/api-reference/zoom-api/chat-messages/getchatmessages#request-parameters

        Use params=kwargs

        Examples:

        https://api.zoom.us/v2/chat/users/{user_id}/messages?to_channel={some_channel_id}

        https://api.zoom.us/v2/chat/users/{user_id}/messages?to_contact={some_contact_id}
        """
        require_keys(kwargs, "user_id")
        return self.get_request(
            "/chat/users/{}/messages?page_size=50".format(kwargs.get("user_id")),
            params=kwargs,
        )

    @Throttled
    def post(self, **kwargs) -> requests.Response:
        """
        https://marketplace.zoom.us/docs/api-reference/zoom-api/chat-messages/sendachatmessage#request-body

        Use data=kwargs

        Examples:

        https://api.zoom.us/v2/chat/users/me/messages

        body: {
            "message": {some_message},
            "to_channel": {some_channel_id}
        }

        body: {
            "message": {some_message},
            "to_contact": {some_contact_id}
        }
        """
        require_keys(kwargs, "message")
        return self.post_request("/chat/users/me/messages", data=kwargs)

    @Throttled
    def update(self, **kwargs) -> requests.Response:
        """
        https://marketplace.zoom.us/docs/api-reference/zoom-api/chat-messages/editmessage#request-body

        Use data=kwargs

        Examples:

        https://api.zoom.us/v2/chat/users/me/messages/{messageId}

        body: {
            "message": {some_message},
            "to_channel": {some_channel_id}
        }

        body: {
            "message": {some_message},
            "to_contact": {some_contact_id}
        }
        """
        require_keys(kwargs, "message_id")
        return self.put_request(
            "/chat/users/me/messages/{}".format(kwargs.get("message_id")), data=kwargs
        )

    @Throttled
    def delete(self, **kwargs) -> requests.Response:
        """
        https://marketplace.zoom.us/docs/api-reference/zoom-api/chat-messages/deletechatmessage#request-parameters

        Use params=kwargs

        Examples:

        https://api.zoom.us/v2/chat/users/me/messages/{message_id}?to_channel={some_channel_id}

        https://api.zoom.us/v2/chat/users/me/messages/{message_id}?to_contact={some_contact_id}
        """
        require_keys(kwargs, "message_id")
        return self.delete_request(
            "/chat/users/me/messages/{}".format(kwargs.get("message_id")), params=kwargs
        )
