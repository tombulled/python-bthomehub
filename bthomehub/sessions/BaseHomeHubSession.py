from .. import lib
import requests
import json

"""
Imports:
    ..lib
    requests
    json

Contains:
    <BaseHomeHubSession>
"""

class BaseHomeHubSession(requests.Session):
    """
    Base Home Hub Session

    Wrapper for <requests.Session>

    Specially designed for use with the Home Hub's
    ... json request
    """

    def __init__(self, *args, user='guest', password='', **kwargs):
        """
        Initialise self and super
        """

        self._init_attrs()

        self.user = user
        self.password = password
        self.password_md5 = lib.gen_md5(password)

        super().__init__(*args, **kwargs)

        self.cookies.update \
        (
            {
                'lang': 'en',
            }
        )

        self._update_session()

    def json_request(self, url, actions):
        """
        Send a json request to the Home Hub
        """

        request = self._gen_request(actions=actions)

        resp_req = self.post(url, data={'req': json.dumps({'request': request})})

        resp_json = resp_req.json()

        self._increment_request()

        self._update_session()

        return resp_json

    def _increment_request(self):
        """
        Increment the request ID

        The request ID stores how many requests have
        ... already been requested
        """

        self.request_id += 1

    def update(self, **kwargs):
        """
        """

        for key, val in kwargs:
            if hasattr(self, key):
                setattr(self, key, val)

    def _gen_session(self):
        """
        Generate the session data to be stored
        ... in the session cookie
        """

        ha1 = lib.gen_session_ha1 \
        (
            user = self.user,
            md5_pass = self.password_md5,
            nonce = self.nonce,
        )

        session_data = \
        {
            'req_id': self.request_id,
            'sess_id': str(self.session_id),
            'basic': False,
            'user': self.user,
            'dataModel': \
            {
                'name': 'Internal',
                'nss': \
                [
                    {
                        'name': 'gtw',
                        'uri': 'http://sagemcom.com/gateway-data',
                    }
                ]
            },
            'ha1': ha1,
            'nonce': self.nonce,
        }

        return session_data

    def _gen_request(self, actions=[], priority=False):
        """
        Generate a request using {actions}
        """

        cnonce = lib.gen_nonce()

        request_index = self.request_id - 1

        auth_key = lib.gen_auth_key \
        (
            user = self.user,
            md5_pass = self.password_md5,
            last_nonce = self.nonce,
            request_index = request_index,
            current_nonce = cnonce,
        )

        request_data = \
        {
            'actions': actions,
            'auth-key': auth_key,
            'cnonce': cnonce,
            'id': request_index,
            'priority': priority,
            'session-id': self.session_id,
        }

        return request_data

    def _update_session(self, session=None):
        """
        Update the session to session {session}

        Note: if {session} is None, a new session is generated
        """

        if session is None:
            session = self._gen_session()

        self.cookies.update \
        (
            {
                'session': json.dumps(session),
            }
        )

    def _init_attrs(self):
        """
        Initialise class attributes
        """

        self.user = None
        self.password = None
        self.password_md5 = None
        self.request_id = 1
        self.session_id = 0
        self.nonce = ''
