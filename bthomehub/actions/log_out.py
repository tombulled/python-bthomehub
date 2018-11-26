"""
Contains:
    log_out()
"""

def log_out(id):
    """
    Action: logOut

    Create a JSON array (dictionary) for the action
    """

    action = \
    {
        'id': id,
        'method': 'logOut',
    }

    return action
