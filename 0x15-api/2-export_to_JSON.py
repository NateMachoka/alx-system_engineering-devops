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

    try:
        # Fetch employee data
        user = requests.get(f"{base_url}/users/{employee_id}").json()
        user_name = user.get("username")
        user_id = user.get("id")

        # Fetch TODO list for the employee
        todos = requests.get(f"{base_url}/todos",
                             params={"userId": employee_id}).json()

        # Prepare data for JSON
        tasks_list = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user_name
            }
            for todo in todos
        ]

        json_data = {str(user_id): tasks_list}

        # Write JSON data to file
        json_filename = f"{user_id}.json"
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4)

    except Exception as error:
        print(error)
        sys.exit(1)
