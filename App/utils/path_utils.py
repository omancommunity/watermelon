#!/home/pi/home/App/env/bin/python3

"""
Ticket System is licensed under the

GNU Lesser General Public License v2.1
Primarily used for software libraries,
the GNU LGPL requires that derived works be licensed under
the same license, but works that only link to it do not fall
under this restriction. There are two commonly used versions of
the GNU LGPL.
"""

from os import path

# This is my working directory in my laptop
WORKING_PATH_MAC = ""

# This the pi device directory
WORKING_PATH_PI = "/home/python/App/"


def check_path_working():
    """
    This function to check
    your working device, in case you transfer this
    application from one to another, in my case;
    I am using laptop and the device .
    Please make sure to change utils.path_utils.py to your
    local directory or as needed
    """
    if path.exists(WORKING_PATH_MAC):
        return WORKING_PATH_MAC
    else:
        return WORKING_PATH_PI


def is_file_exists(file):
    if path.exists(file):
        return True
    else:
        return False


def is_db_file():
    if is_file_exists(check_path_working() + 'data/db/watermoleon.db'):
        return True
    else:
        return False
