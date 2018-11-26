import socket

"""
Imports:
    socket

Contains:
    find_hub()

Constants defined here:
    DEFAULT_HOST_NAME
"""

DEFAULT_HOST_NAME = 'bthub'

def find_hub(host_name = DEFAULT_HOST_NAME):
    """
    Attempts to find the hub on your network

    Converts the host name (bthub) into its IP address
    """

    name, alias_list, address_list = socket.gethostbyaddr(host_name)

    return address_list[0]
