#!/usr/bin/python3

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
    else:
        employee_id = int(argv[1])

        # Fetch user info
        user_response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
        )
        user_data = user_response.json()

        # Fetch TODO list
        todo_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
        )
        todo_data = todo_response.json()

        # Filter completed tasks
        completed_tasks = [task for task in todo_data if task["completed"]]

        # Display information
        print("Employee {} is done with tasks({}/{}):".format(
            user_data["name"], len(completed_tasks), len(todo_data)
        ))

        for task in completed_tasks:
            print("\t {}".format(task["title"]))

