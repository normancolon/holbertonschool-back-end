#!/usr/bin/python3
"""
Export employee's TODO list progress to a CSV file from an API.
"""
import csv
import requests
import sys


def fetch_data(url):
    """Sends a GET request to the specified URL and returns the JSON response."""
    response = requests.get(url)
    if response.ok:
        return response.json()
    response.raise_for_status()


def write_to_csv(employee_id, username, todos):
    """Writes TODOs to a CSV file formatted with user ID, username, task completion status, and title."""
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [employee_id, username, todo['completed'], todo['title']])


def main(employee_id):
    """Main function to process data and write to CSV."""
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={
        employee_id}'

    employee_data = fetch_data(user_url)
    todos_data = fetch_data(todos_url)

    write_to_csv(employee_id, employee_data['username'], todos_data)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    main(sys.argv[1])
