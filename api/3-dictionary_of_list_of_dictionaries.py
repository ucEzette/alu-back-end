#!/usr/bin/python3
"""
This module exports all employee tasks data to a JSON file.

The exported JSON file will contain tasks for all users fetched from
https://jsonplaceholder.typicode.com/users and their tasks from
https://jsonplaceholder.typicode.com/todos.

Each user's tasks are stored under their user ID in the following format:
{
    "USER_ID": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETION_STATUS
        },
        ...
    ],
    ...
}
"""

import json
import requests

# Define the URLs for fetching users and todos data
USERS_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"


def export_all_tasks_to_json():
    """
    Fetches tasks for all employees and exports them to todo_all_employees.json
    """
    # Fetch users and todos data from the API
    users = requests.get(USERS_URL).json()
    todos = requests.get(TODOS_URL).json()

    # Dictionary to hold tasks for all users
    all_tasks = {}

    # Process each user and their corresponding tasks
    for user in users:
        user_id = user['id']
        username = user['username']
        # Filter tasks for the current user
        user_tasks = []
        for task in todos:
            if task['userId'] == user_id:
                user_tasks.append({
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                })
        # Store the tasks in the all_tasks dictionary
        all_tasks[user_id] = user_tasks

    # Write the output to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_tasks_to_json()
