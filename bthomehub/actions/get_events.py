"""
Contains:
    get_events()
"""

def get_events(id):
    """
    Action: getEvents

    Create a JSON array (dictionary) for the action
    """

    action = \
    {
        'id': id,
        'method': 'getEvents',
    }

    return action
