"""
Contains:
    get_value()
"""

def get_value(id, xpath):
    """
    Action: getValue

    Create a JSON array (dictionary) for the action
    """

    action = \
    {
        'id': id,
        'method': 'getValue',
        'xpath': xpath,
        'options': \
        {
            'capability-flags': \
            {
                'interface': True,
            }
        }
    }

    return action
