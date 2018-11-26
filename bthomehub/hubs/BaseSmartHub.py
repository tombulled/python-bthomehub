from .. import sessions
from .. import actions

"""
Imports:
    ..sessions
    ..actions

Contains:
    <BaseSmartHub>
"""

class BaseSmartHub(object):
    """
    Base Smart Hub

    A class to interact with a Home Hub
    Makes use of a <sessions.HomeHubSession>
    """

    def __init__(self, host):
        """
        Initialise self
        """

        self._init_attrs()

        self.host = host

        self.HomeHubSession = sessions.HomeHubSession(user='guest', password='')

    def _make_url(self, dir='0000016400/gui/#/', endpoint=''):
        """
        Make a HTTP url in the format:
            http://{host}/{dir}{endpoint}
        """

        url = f'http://{self.host}/{dir}{endpoint}'

        return url

    def _session(self):
        """
        Returns self.HomeHubSession (shorthand)
        """

        return self.HomeHubSession

    def json_request(self, actions):
        """
        Send a JSON request to the Hub with {actions}
        """

        url = self._make_url(dir='cgi/', endpoint='json-req')

        json_resp = self._session().json_request(url, actions)

        return json_resp

    def _init_attrs(self):
        """
        Initialise class attributes
        """

        self.host = None
        self.user = 'guest'
        self.password = ''

    def arping(self, xpath):
        """
        Call action: arping(xpath)
        """

        action_arping = actions.arping(id=0, xpath=xpath)

        actions_list = [action_arping]

        json_resp = self.json_request(actions_list)

        return json_resp

    def get_events(self):
        """
        Call action: getEvents()

        Warning: I take 5 mins to reply! -- NEVER call me
        """

        action_get_events = actions.get_events(id = 0)

        actions_list = [action_get_events]

        json_resp = self.json_request(actions_list)

        return json_resp

    def get_values(self, xpaths):
        """
        Call action: getValues(xpaths)
        """

        actions_list = []

        for index, xpath in enumerate(xpaths):
            action_get_value = actions.get_value(id=index, xpath=xpath)

            actions_list.append(action_get_value)

        json_resp = self.json_request(actions_list)

        return json_resp

    def get_value(self, xpath):
        """
        Call action: getValue(xpath)
        """

        action_get_value = actions.get_value(id=0, xpath=xpath)

        actions_list = [action_get_value]

        json_resp = self.json_request(actions_list)

        return json_resp

    def log_in(self, user):
        """
        Call action: logIn(user)
        """

        action_log_in = actions.log_in(id=0, user=user)

        actions_list = [action_log_in]

        json_resp = self.json_request(actions_list)

        return json_resp

    def log_out(self):
        """
        Call action: logOut()
        """

        action_log_out = actions.log_out(id=0)

        actions_list = [action_log_out]

        json_resp = self.json_request(actions_list)

        return json_resp

    def subscribe_for_notification(self, xpath, parameter_id):
        """
        Call action: subscribeForNotification(xpath, parameter_id)
        """

        action = actions.subscribe_for_notification(id=0, xpath=xpath, parameter_id=parameter_id)

        actions_list = [action]

        json_resp = self.json_request(actions_list)

        return json_resp

    def unsubscribe_for_notifications(self, parameter_ids):
        """
        Call action: unsubscribeForNotifications(parameter_ids)
        """

        actions_list = []

        for index, parameter_id in enumerate(parameter_ids):
            action = actions.unsubscribe_for_notification(id=index, parameter_id=parameter_id)

            actions_list.append(action)

        json_resp = self.json_request(actions_list)

        return json_resp

    def unsubscribe_for_notification(self, parameter_id):
        """
        Call action: unsubscribeForNotification(parameter_id)
        """

        action = actions.unsubscribe_for_notification(id=0, parameter_id=parameter_id)

        actions_list = [action]

        json_resp = self.json_request(actions_list)

        return json_resp

    def upload_bm_statistics_file(self, xpath, start_date, end_date):
        """
        Call action: uploadBMStatisticsFile(xpath, start_date, end_date)
        """

        action = actions.upload_bm_statistics_file(id=0, xpath=xpath, start_date=start_date, end_date=end_date)

        actions_list = [action]

        json_resp = self.json_request(actions_list)

        return json_resp
