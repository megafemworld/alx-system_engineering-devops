#!/usr/bin/python3
""" API returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    todo_url = f"{base_url}/todos?userId={id}"
    user_url = f"{base_url}/users/{id}"
    un = requests.get(user_url).json().get('username')
    filename = f"{id}.csv"
    todos = requests.get(todo_url).json()
    with open(filename, 'w') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            w.writerow([id, un, t['completed'], t['title']])
