"""
Contains:
    log_in()
"""

def log_in(id, user):
    """
    Action: logIn

    Create a JSON array (dictionary) for the action
    """

    action = \
    {
        'id': id,
        'method': 'logIn',
        'parameters': \
        {
            'persistent': 'true',
            'session-options': \
            {
                'capability-depth': 2,
                'capability-flags': \
                {
                    'default-value': False,
                    'description': False,
                    'name': True,
                    'restriction': True,
                },
                'context-flags': \
                {
                    'get-content-name': True,
                    'local-time': True,
                },
                'language': 'ident',
                'nss': \
                [
                    {
                        'name': 'gtw',
                        'uri': 'http://sagemcom.com/gateway-data',
                    },
                ],
                'time-format': 'ISO_8601',
            },
            'user': user,
        },
    }

    return action
