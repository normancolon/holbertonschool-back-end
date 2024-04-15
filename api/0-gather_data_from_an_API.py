#!/usr/bin/python3
"""
data gathering from api module
"""
import requests
import sys


def fetch_and_display_todo(employee_id):
    """Fetch and display employee's TODO list progress."""
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={
        employee_id}'

    user_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    completed_todos = [task for task in todos_data if task['completed']]
    completed_count = len(completed_todos)
    total_tasks = len(todos_data)

    print(f"Employee {user_data['name']} is done with tasks({
          completed_count}/{total_tasks}):")
    for task in completed_todos:
        print(f'\t {task["title"]}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        fetch_and_display_todo(sys.argv[1])
    else:
        print("Usage: ./script.py <employee_id>")
