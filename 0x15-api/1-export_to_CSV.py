#!/usr/bin/python3
"""
Fetches TODO list data for a given employee ID and exports it to a CSV file.
"""

import csv
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
    user_name = user.get("username")

    todos = requests.get(f"{base_url}/todos",
                         params={"userId": employee_id}).json()

    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                user_name,
                task.get("completed"),
                task.get("title")
            ])
