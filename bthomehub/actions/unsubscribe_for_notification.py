"""
Contains:
    unsubscribe_for_notification()
"""

def unsubscribe_for_notification(id, parameter_id):
    """
    Action: unsubscribeForNotification

    Create a JSON array (dictionary) for the action
    """

    action = \
    {
        'id': id,
        'method': 'unsubscribeForNotification',
        'parameters': \
        {
            'id': str(parameter_id),
        }
    }

    return action
