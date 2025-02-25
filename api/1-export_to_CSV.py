#!/usr/bin/python3
"""
This script fetches the TODO list progress for a given employee from a REST API
and exports the data into a CSV file.

The CSV format is:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
The CSV file is named USER_ID.csv
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f"Employee ID {employee_id} not found.")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("username")

    # Fetch TODO list for the employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # CSV file name: USER_ID.csv
    csv_filename = f"{employee_id}.csv"

    # Write to CSV file
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title")
            ])

    print(f"Data exported to {csv_filename}.")
