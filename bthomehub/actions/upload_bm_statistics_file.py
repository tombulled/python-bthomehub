"""
Contains:
    upload_bm_statistics_file()
"""

def upload_bm_statistics_file(id, xpath, start_date, end_date):
    """
    Action: uploadBMStatisticsFile

    Create a JSON array (dictionary) for the action
    """

    action = \
    {
        'id': id,
        'method': 'uploadBMStatisticsFile',
        'parameters': \
        {
            'endDate': end_date,
            'startDate': start_date,
        },
        'xpath': xpath,
    }

    return action
