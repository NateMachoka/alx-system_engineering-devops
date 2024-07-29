#!/usr/bin/python3
"""
Fetches and displays the TODO list progress of a given employee ID and
exports the data in JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    user_name = user.get("username")  # Changed from 'name' to 'username'

    # Fetch TODO list for the employee
    todos = requests.get(f"{base_url}/todos",
                         params={"userId": employee_id}).json()

    # Prepare data for JSON
    json_data = {
        str(employee_id): [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user_name
            }
            for todo in todos
        ]
    }

    # Write JSON data to file
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
