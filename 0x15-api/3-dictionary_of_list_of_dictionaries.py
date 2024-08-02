#!/usr/bin/python3
""" API returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    import json

    base_url = "https://jsonplaceholder.typicode.com/"
    todo_url = f"{base_url}/todos"
    user_url = f"{base_url}/users"
    users = requests.get(user_url).json()
    filename = "todo_all_employees.json"
    todos = requests.get(todo_url).json()
    alldict = {}
    for user in users:
        tasks = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskdict = {
                        "username": user.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')}
                tasks.append(taskdict)
            alldict[user.get('id')] = tasks

    with open(filename, 'w') as f:
        json.dump(alldict, f)
