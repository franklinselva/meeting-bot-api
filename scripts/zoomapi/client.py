# THIS FILE WAS CHANGED FROM THE ORIGINAL

"""Zoom.us REST API Python Client"""

from zoomapi import components, util

API_BASE_URIS = "https://api.zoom.us/v2"

COMPONENT_CLASSES = {
    "user": components.user.UserComponentV2,
    "meeting": components.meeting.MeetingComponentV2,
    "report": components.report.ReportComponentV2,
    "webinar": components.webinar.WebinarComponentV2,
    "recording": components.recording.RecordingComponentV2,
}


class ZoomClient(util.ApiClient):
    """Zoom.us REST API Python Client"""

    """Base URL for Zoom API"""

    def __init__(self, api_key, api_secret, base_uri = None, data_type="json", timeout=15):
        """Create a new Zoom client

        :param api_key: The Zooom.us API key
        :param api_secret: The Zoom.us API secret
        :param data_type: The expected return data type. Either 'json' or 'xml'
        :param timeout: The time out to use for API requests
        """
        if base_uri is None:
            self.BASE_URI = API_BASE_URIS
        else:
            self.BASE_URI = base_uri
            
        self.components = COMPONENT_CLASSES.copy()

        super(ZoomClient, self).__init__(base_uri=self.BASE_URI, timeout=timeout)

        # Setup the config details
        self.config = {
            "api_key": api_key,
            "api_secret": api_secret,
            "data_type": data_type,
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    def refresh_token(self):
        pass

    @property
    def api_key(self) -> str:
        """The Zoom.us api_key"""
        return self.config.get("api_key")

    @api_key.setter
    def api_key(self, value):
        """Set the api_key"""
        self.config["api_key"] = value
        self.refresh_token()

    @property
    def api_secret(self) -> str:
        """The Zoom.us api_secret"""
        return self.config.get("api_secret")

    @api_secret.setter
    def api_secret(self, value):
        """Set the api_secret"""
        self.config["api_secret"] = value
        self.refresh_token()

    @property
    def meeting(self) -> components.meeting.MeetingComponentV2:
        """Get the meeting component"""
        return self.components.get("meeting")

    @property
    def report(self) -> components.report.ReportComponentV2:
        """Get the report component"""
        return self.components.get("report")

    @property
    def user(self) -> components.user.UserComponentV2:
        """Get the user component"""
        return self.components.get("user")

    @property
    def webinar(self) -> components.webinar.WebinarComponentV2:
        """Get the webinar component"""
        return self.components.get("webinar")

    @property
    def recording(self) -> components.recording.RecordingComponentV2:
        """Get the recording component"""
        return self.components.get("recording")
