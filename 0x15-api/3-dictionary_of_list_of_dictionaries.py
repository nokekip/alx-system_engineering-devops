#!/usr/bin/python3
"""
Fetch and Export to JSON employee TODO list progress using a REST API.
"""
import json
import requests


def export_to_json():
    """return API data"""
    base_url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(base_url + f"users").json()

    """Export to JSON file"""
    with open("todo_all_employees.json", "w") as empfile:
        json.dump({
            user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get(base_url + "todos",
                                       params={"userId": user.get("id")})
                .json()]
            for user in users}, empfile)


if __name__ == '__main__':
    export_to_json()
