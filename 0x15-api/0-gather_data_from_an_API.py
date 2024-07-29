#!/usr/bin/python3
"""Makes an API request and returns information about an employee's
TODO list progress
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    EMPLOYEE_ID = argv[1]
    URL = 'https://jsonplaceholder.typicode.com/users'
    try:
        user = requests.get('{}/{}'.format(URL, EMPLOYEE_ID)).json()
        user_todos = requests.get('{}/{}/todos'.format(
            URL, EMPLOYEE_ID)).json()
        completed_tasks = []
        for todo in user_todos:
            if todo.get('completed') is True:
                completed_tasks.append(todo)
        user_name = user.get('name')
        total_completed_tasks = len(completed_tasks)
        total_tasks = len(user_todos)
        print('Employee {} is done with tasks({}/{}):'.format(
            user_name, total_completed_tasks, total_tasks))
        for completed_task in completed_tasks:
            print('\t {}'.format(completed_task.get('title')))
    except Exception as error:
        pass
