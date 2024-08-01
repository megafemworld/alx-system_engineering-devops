#!/usr/bin/python3
""" API returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    todo_url = f"{base_url}/todos?userId={employee_id}"
    user_url = f"{base_url}/users/{employee_id}"
    username = requests.get(user_url).json().get('username')
    filename = f"{employee_id}.csv"
    todos = requests.get(todo_url).json()
    with open(filename, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, username, todo['completed'], todo['title']])
