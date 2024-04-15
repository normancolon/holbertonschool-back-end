#!/usr/bin/python3
"""
This script retrieves task completion information for a specific employee from
https://jsonplaceholder.typicode.com/ and prints out the completed tasks.
"""
import requests
import sys


def get_employee_tasks(employee_id):
    """Retrieve and display tasks for a given employee ID."""
    root_url = "https://jsonplaceholder.typicode.com/"
    try:
        employee_info = requests.get(f'{root_url}users/{employee_id}').json()
        todos = requests.get(f'{root_url}todos', params={
                             'userId': employee_id}).json()
    except requests.RequestException:
        print("Error fetching data from the API.")
        return

    if 'name' not in employee_info:
        print("No employee found with the given ID.")
        return

    employee_name = employee_info['name']
    completed_tasks = [task['title']
                       for task in todos if task.get('completed', False)]
    total_tasks = len(todos)

    # Correcting string to be properly terminated
    print(f"Employee {employee_name} is done with tasks("
          f"{len(completed_tasks)}/{total_tasks}):")
    for title in completed_tasks:
        print(f"\t {title}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            get_employee_tasks(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Usage: ./script.py <employee_id>")
