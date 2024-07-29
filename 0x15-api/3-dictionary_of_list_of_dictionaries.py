#!/usr/bin/python3
"""Makes an API request and returns information about all employee's
TODO list progress
"""
import json
import requests


def fetch_data():
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    users_response = requests.get(url_users)
    todos_response = requests.get(url_todos)

    users = users_response.json()
    todos = todos_response.json()

    return users, todos


def process_data(users, todos):
    user_mapping = {str(user['id']): user['username'] for user in users}
    processed_data = {}

    for todo in todos:
        user_id = str(todo['userId'])
        if user_id not in processed_data:
            processed_data[user_id] = []

        processed_data[user_id].append({
            "username": user_mapping.get(user_id, "Unknown"),
            "task": todo['title'],
            "completed": todo['completed']
        })
    return processed_data


def save_to_json(data, filename='todo_all_employees.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    users, todos = fetch_data()
    processed_data = process_data(users, todos)
    save_to_json(processed_data)
