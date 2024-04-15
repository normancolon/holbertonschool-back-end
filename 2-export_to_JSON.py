#!/usr/bin/python3
"""
Export TODOs to JSON.
"""
import json
import requests
import sys


def fetch_data(url):
    """Fetch data from API."""
    response = requests.get(url)
    if response.ok:
        return response.json()
    response.raise_for_status()


def export_to_json(employee_id, username, todos):
    """Export data to JSON file."""
    filename = f"{employee_id}.json"
    tasks = [
        {"task": todo['title'], "completed": todo['completed'],
            "username": username}
        for todo in todos
    ]
    with open(filename, 'w') as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)


def main(employee_id):
    """Main execution function."""
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={
        employee_id}'

    employee_data = fetch_data(user_url)
    todos_data = fetch_data(todos_url)

    export_to_json(employee_id, employee_data['username'], todos_data)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    main(sys.argv[1])
