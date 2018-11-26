"""
Contains:
    arping()
"""

def arping(id, xpath):
    """
    Action: arping

    Create a JSON array (dictionary) for the action
    """

    action = \
    {
        'id': id,
        'method': 'arping',
        'xpath': xpath,
    }

    return action
