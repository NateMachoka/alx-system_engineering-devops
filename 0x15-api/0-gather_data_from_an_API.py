#!/usr/bin/python3
"""
Fetches and displays the TODO list progress of a given employee ID.
"""

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

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    user_name = user.get("name")

    todos = requests.get(f"{base_url}/todos",
                         params={"userId": employee_id}).json()

    # Filter completed tasks
    completed_tasks = [t.get("title") for t in todos if t.get("completed")]
    total_tasks = len(todos)
    number_of_done_tasks = len(completed_tasks)

    # Output results
    print(
        f"Employee {user_name} is done with tasks("
        f"{number_of_done_tasks}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task}")
