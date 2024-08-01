#!/usr/bin/python3
""" API returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    todo_url = f"{base_url}/todos?userId={employee_id}"
    filename = f"{employee_id}.csv"
    todos = requests.get(todo_url).json()
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writenow([argv[1], todo['completed'], todo['title']])
