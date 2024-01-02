#!/usr/bin/env python3
import requests
import csv
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

        # Create CSV file
        csv_file_name = "{}.csv".format(employee_id)
        with open(csv_file_name, mode='w', newline='') as csv_file:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()

            # Write tasks to CSV
            for task in todo_data:
                writer.writerow({
                    'USER_ID': user_data["id"],
                    'USERNAME': user_data["username"],
                    'TASK_COMPLETED_STATUS': str(task["completed"]),
                    'TASK_TITLE': task["title"]
                })

        print("Data exported to {}".format(csv_file_name))
