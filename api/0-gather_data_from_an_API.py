#!/usr/bin/python3
"""
This module fetches an employee's TODO list progress from a REST API and
displays it in a specified format.
"""
import requests
import sys


def fetch_data(employee_id):
    """
    Fetches employee and their TODOs from the API using the provided employee_id.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        return None, None
    user_data = user_response.json()

    # Fetch TODOs for the user
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        return user_data, None
    todos_data = todos_response.json()

    return user_data, todos_data


def main():
    """
    Main function to handle command-line arguments and output the TODO list progress.
    """
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        return

    employee_id = sys.argv[1]
    user_data, todos_data = fetch_data(employee_id)

    if user_data is None or todos_data is None:
        print(f"Failed to retrieve data for user ID {employee_id}")
        return

    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)

    print(f"Employee {user_data['name']} is done with tasks({
          len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    main()
