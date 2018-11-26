from .SkimmedSmartHub import SkimmedSmartHub
from .. import lib

"""
Imports:
    .SkimmedSmartHub.SkimmedSmartHub
    ..lib

Contains:
    <SmartHub>
"""

class SmartHub(object):
    """
    Highest-level Smart Hub

    Indirectly inherits from <SkimmedSmartHub>
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise self
        Initialise indirect super: <SkimmedSmartHub>
        """

        self._init_attrs()

        self.SkimmedSmartHub = SkimmedSmartHub(*args, **kwargs)

        self.host = self._super().host

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form:
            <class_name(user:password@host:port)>
        """

        return f'<{self.__class__.__name__}({self.user}:{self.password}@{self.host}:{self.port})>'

    def login(self, user='guest', password=''):
        """
        Login to the Home Hub

        Note: defaults to 'guest' login
        """

        self.user = user
        self.password = password

        self._super().user = user
        self._super().password = password
        self._super().request_id = 0
        self._super().session_id = '0'
        self._super()._session().user = user
        self._super()._session().password = password
        self._super()._session().password_md5 = lib.gen_md5(password)

        self._super()._session()._update_session()

        resp = self._super().log_in(user)

        if not resp:
            return False

        self._super()._session().session_id = resp['session_id']
        self._super()._session().nonce = resp['nonce']

        return True

    def logout(self):
        """
        Logout of the Home Hub

        Note: this will reset the session
        """

        resp = self._super().log_out()

        self._super()._session().session_id = 0
        self._super()._session().nonce = ''
        self._super()._session().request_id = 1
        self._super()._session()._update_session()

        return resp

    def get_value(self, *args, **kwargs):
        """
        Wrapper for self.SkimmedSmartHub.get_value
        """

        return self._super().get_value(*args, **kwargs)

    def get_values(self, *args, **kwargs):
        """
        Wrapper for self.SkimmedSmartHub.get_values
        """

        return self._super().get_values(*args, **kwargs)

    def _init_attrs(self):
        """
        Initialise class attributes
        """

        self.SkimmedSmartHub = None
        self.user = None
        self.password = None
        self.host = None
        self.port = 80

    def _super(self):
        """
        Returns self.SkimmedSmartHub
        """

        return self.SkimmedSmartHub
