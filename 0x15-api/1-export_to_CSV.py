#!/usr/bin/python3
"""
Fetch and export employee TODO list progress using a REST API to CSV.
"""

import csv
import requests
import sys


def user_info():
    """return API data"""
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user = requests.get(base_url + f"users/{user_id}").json()
    todos = requests.get(base_url + f"users/{user_id}/todos").json()

    """Export fetched data to CSV file"""
    with open(f"{user_id}.csv", 'w') as csvfile:
        for todo in todos:
            csvfile.write('"{}","{}","{}","{}\n'
                          .format(user_id, user.get('username'),
                                  todo.get('completed'),
                                  todo.get('title')))


if __name__ == '__main__':
    user_info()
