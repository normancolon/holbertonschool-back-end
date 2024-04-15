#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress from an API.
"""
import requests
import sys


def fetch_employee_data(employee_id):

    try:
        employee_url = f'https://jsonplaceholder.typicode.com/users/{
            employee_id}'
        todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={
            employee_id}'
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)

        if not employee_response.ok:
            return f"Error: Could not retrieve user data for ID {employee_id}"

        if not todos_response.ok:
            return f"Error: Could not retrieve TODOs for user ID {employee_id}"

        return employee_response.json(), todos_response.json()
    except requests.RequestException as e:
        return f"Error: {str(e)}"


def print_employee_todo_report(employee_data, todos_data):
    """Print TODO progress using employee and TODO data."""
    if isinstance(employee_data, str):
        print(employee_data)  # If an error message is returned, print it
        return

    employee_name = employee_data['name']
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    total_tasks = len(todos_data)

    print(f"Employee {employee_name} is done with tasks({
          len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")


def main():

    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        return

    employee_id = sys.argv[1]
    data = fetch_employee_data(employee_id)
    print_employee_todo_report(*data)


if __name__ == "__main__":
    main()
