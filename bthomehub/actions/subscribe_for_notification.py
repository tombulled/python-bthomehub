"""
Contains:
    subscribe_for_notification()
"""

def subscribe_for_notification(id, xpath, parameter_id):
    """
    Action: subscribeForNotification

    Create a JSON array (dictionary) for the action
    """

    action = \
    {
        'id': id,
        'method': 'subscribeForNotification',
        'parameters': \
        {
            'current-value': False,
            'id': str(parameter_id),
            'type': 'value-change',
        },
        'xpath': xpath,
    }

    return action
