#!/usr/bin/env python3
import requests
import json

if __name__ == "__main__":
    # Fetch all users
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users_data = users_response.json()

    # Create a dictionary to store tasks for each user
    all_tasks = {}

    # Iterate through each user
    for user in users_data:
        user_id = user["id"]

        # Fetch TODO list for each user
        todo_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
        )
        todo_data = todo_response.json()

        # Store tasks for the user
        all_tasks[user_id] = [{"username": user["username"], "task": task["title"], "completed": task["completed"]} for task in todo_data]

    # Create JSON file for all tasks
    json_file_name = "todo_all_employees.json"
    with open(json_file_name, mode='w') as json_file:
        json.dump(all_tasks, json_file)

    print("Data exported to {}".format(json_file_name))

