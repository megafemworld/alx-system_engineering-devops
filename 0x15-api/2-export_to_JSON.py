#!/usr/bin/python3
""" API returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    todo_url = f"{base_url}/todos?userId={id}"
    user_url = f"{base_url}/users/{id}"
    un = requests.get(user_url).json().get('username')
    filename = f"{id}.json"
    todos = requests.get(todo_url).json()
    tasks = []
    for todo in todos:
        task = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": un
        }
        tasks.append(task)
    data = {str(id): tasks}

    with open(filename, 'w') as f:
        json.dump(data, f)
