#!/usr/bin/python3
"""
Export all TODOs.
"""
import json
import requests


def fetch_data(url):
    """Fetch JSON data."""
    response = requests.get(url)
    if response.ok:
        return response.json()
    response.raise_for_status()


def compile_user_tasks(users, todos):
    """Compile tasks per user."""
    user_tasks = {}
    for user in users:
        user_tasks[user['id']] = [
            {
                'username': user['username'],
                'task': todo['title'],
                'completed': todo['completed']
            }
            for todo in todos if todo['userId'] == user['id']
        ]
    return user_tasks


def export_to_json(data):
    """Export data to JSON."""
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)


def main():
    """Main execution function."""
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users = fetch_data(users_url)
    todos = fetch_data(todos_url)
    user_tasks = compile_user_tasks(users, todos)
    export_to_json(user_tasks)


if __name__ == "__main__":
    main()
