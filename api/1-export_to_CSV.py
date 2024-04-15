#!/usr/bin/python3
"""
This module fetches an employee's TODO list
from a JSONPlaceholder API and exports it to a CSV file.
"""
import csv
import requests
import sys


def fetch_data(employee_id):
    """Fetch user and TODO data from API."""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Fetch user info
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        return None, None  # API request failed
    user_data = user_response.json()

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        return user_data, None  # API request failed
    todos_data = todos_response.json()

    return user_data, todos_data


def export_to_csv(user_data, todos_data):
    """Export user's TODOs to a CSV file."""
    filename = f"{user_data['id']}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # Write rows to CSV
        for todo in todos_data:
            writer.writerow([user_data['id'], user_data['username'],
                             todo['completed'], todo['title']])


def main():
    """Main function to execute script logic."""
    if len(sys.argv) < 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        return

    employee_id = sys.argv[1]
    user_data, todos_data = fetch_data(employee_id)

    if user_data is None or todos_data is None:
        print(f"Failed to retrieve data for user ID {employee_id}")
        return

    export_to_csv(user_data, todos_data)
    print(f"Data successfully written to {user_data['id']}.csv")


if __name__ == "__main__":
    main()
