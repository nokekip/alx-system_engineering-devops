#!/usr/bin/python3
"""
Fetch and display employee TODO list progress using a REST API.
"""
import json
import requests
import sys


def user_info():
    """return API data"""
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user = requests.get(base_url + f"users/{user_id}").json()
    todos = requests.get(base_url + f"users/{user_id}/todos").json()

    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    for todo in todos:
        TOTAL_NUM_OF_TASKS += 1
        if todo['completed'] is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(todo['title'])

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), NUMBER_OF_DONE_TASKS, TOTAL_NUM_OF_TASKS))
    for task in TASK_TITLE:
        print(f"\t {task}")


if __name__ == '__main__':
    user_info()
