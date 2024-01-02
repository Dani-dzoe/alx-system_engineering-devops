#!/usr/bin/env python3
import requests
import json
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

        # Create JSON file
        json_file_name = "{}.json".format(employee_id)
        with open(json_file_name, mode='w') as json_file:
            json.dump({ 
                "USER_ID": [{"task": task["title"], "completed": task["completed"], "username": user_data["username"]} for task in todo_data]
            }, json_file)

        print("Data exported to {}".format(json_file_name))

