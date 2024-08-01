#!/usr/bin/python3
""" API returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    from sys import argv

    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    name_url = f"{base_url}/users/{employee_id}"
    name = requests.get(name_url).json().get('name')
    todo_url = f"{base_url}/todos?userId={employee_id}"
    todos = len(requests.get(todo_url).json())
    com_url = f"{todo_url}&completed=true"
    completed = (requests.get(com_url).json())
    completed_t = len(completed)
    done_tasks = [todo for todo in completed]
    print(f"Employee {name} is done with tasks({completed_t}/{todos}):")
    for title in done_tasks:
        print(f"\t {title.get('title')}")
