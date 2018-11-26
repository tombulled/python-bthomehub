from .BaseSmartHub import BaseSmartHub

"""
Imports:
    .BaseSmartHub.BaseSmartHub

Contains:
    <SkimmedSmartHub>
"""

class RequestFailed(Exception): pass # Move me to ~errors~

class SkimmedSmartHub(BaseSmartHub):
    """
    Skimmed Smart Hub

    Inherits from: <BaseSmartHub>
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise self and super
        """

        super().__init__(*args, **kwargs)

    def get_value(self, xpath):
        """
        Call action: getValue(xpath)

        Returns: resp_json['reply']['actions'][0]['callbacks'][0]['parameters']['value']

        On 'request failed', raises <RequestFailed>
        """

        resp_json = super().get_value(xpath)

        if self._request_failed(resp_json):
            error_code = resp_json['reply']['error']['code']
            error_description = resp_json['reply']['error']['description']

            raise RequestFailed(f'[{error_code}] {error_description}')

        value = resp_json['reply']['actions'][0]['callbacks'][0]['parameters']['value']

        return value

    def get_values(self, *xpaths):
        """
        Call action: getValues(xpaths)

        Returns: List of values

        On 'request failed', raises <RequestFailed>
        """

        resp_json = super().get_values(xpaths)

        if self._request_failed(resp_json):
            error_code = resp_json['reply']['error']['code']
            error_description = resp_json['reply']['error']['description']

            raise RequestFailed(f'[{error_code}] {error_description}')

        values = []

        for action in resp_json['reply']['actions']:
            value = action['callbacks'][0]['parameters']['value']

            values.append(value)

        return values

    def subscribe_for_notification(self, xpath, parameter_id):
        """
        Call action: subscribeForNotification(xpath, parameter_id)

        Returns: success

        On 'request failed', raises <RequestFailed>
        """

        resp_json = super().subscribe_for_notification(xpath, parameter_id)

        if self._request_failed(resp_json):
            error_code = resp_json['reply']['error']['code']
            error_description = resp_json['reply']['error']['description']

            raise RequestFailed(f'[{error_code}] {error_description}')

        error_code = resp_json['reply']['actions'][0]['error']['code']

        return error_code == 16777238

    def unsubscribe_for_notification(self, parameter_id):
        """
        Call action: unsubscribeForNotification(parameter_id)

        Returns: success

        On 'request failed', raises <RequestFailed>
        """

        resp_json = super().unsubscribe_for_notification(parameter_id)

        if self._request_failed(resp_json):
            error_code = resp_json['reply']['error']['code']
            error_description = resp_json['reply']['error']['description']

            raise RequestFailed(f'[{error_code}] {error_description}')

        error_code = resp_json['reply']['actions'][0]['error']['code']

        return error_code == 16777238

    def unsubscribe_for_notifications(self, *parameter_ids):
        """
        Call action: unsubscribeForNotifications(parameter_ids)

        Returns: List of successes

        On 'request failed', raises <RequestFailed>
        """

        resp_json = super().unsubscribe_for_notifications(parameter_ids)

        if self._request_failed(resp_json):
            error_code = resp_json['reply']['error']['code']
            error_description = resp_json['reply']['error']['description']

            raise RequestFailed(f'[{error_code}] {error_description}')

        successes = []

        for action in resp_json['reply']['actions']:
            error_code = action['error']['code']

            success = error_code == 16777238

            successes.append(success)

        return successes

    def arping(self, xpath):
        """
        ***NOT IMPLEMENTED***
        """

        return ### THIS IS BROKEN FOR NOW

    def get_events(self):
        """
        ***NOT IMPLEMENTED***
        """

        return ### THIS NEVER RETURNS

    def log_in(self, user):
        """
        Call action: logIn(user)

        Returns:
            {
                'session_id': {session_id},
                'nonce': {nonce},
            }

            OR, False on error
        """

        resp_json = super().log_in(user)

        error_code = resp_json['reply']['actions'][0]['error']['code']

        success = error_code == 16777238

        if not success:
            return False

        session_id = resp_json['reply']['actions'][0]['callbacks'][0]['parameters']['id']
        nonce = resp_json['reply']['actions'][0]['callbacks'][0]['parameters']['nonce']

        data = {'session_id': session_id, 'nonce': nonce}

        return data

    def log_out(self):
        """
        Call action: logOut()

        Returns: success
        """

        resp_json = super().log_out()

        error_code = resp_json['reply']['actions'][0]['error']['code']

        return error_code == 16777238

    def upload_bm_statistics_file(self, xpath, start_date, end_date):
        """
        Call action: uploadBMStatisticsFile(xpath, start_date, end_date)

        Returns:
            On success -> {download_uri}
            On failure -> False

        On 'request failed', raises <RequestFailed>
        """

        resp_json = super().upload_bm_statistics_file(xpath, start_date, end_date)

        error_code = resp_json['reply']['actions'][0]['error']['code']

        success = error_code == 16777238

        if not success:
            return False

        download_uri = resp_json['reply']['actions'][0]['callbacks'][0]['parameters']['data']

        return download_uri

    def _request_failed(self, resp):
        """
        Check if the request response {resp}
        ... indicates that the request failed
        """

        error_code = resp['reply']['error']['code']

        failed = error_code not in (16777238, 16777216)

        return failed
