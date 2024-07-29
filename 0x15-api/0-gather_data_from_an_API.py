#!/usr/bin/python3
"""
This module fetches and displays the TODO list progress of a given employee
using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress of an employee.

    Args:
        employee_id (int): The ID of the employee.
    """
    # Define the base URL
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch the employee data
    employee_data = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = employee_data.get('name')

    # Fetch the employee's TODO list
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()

    # Calculate the TODO list progress
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
