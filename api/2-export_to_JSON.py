#!/usr/bin/python3
"""
This script takes a user ID as a command-line argument, retrieves the corresponding
username and tasks from the JSONPlaceholder API, and saves the information in a JSON file
named after the user ID.
"""
import json
import requests
import sys


def fetch_user_tasks(user_id):
    """Fetch tasks and username for a given user ID and write to a JSON file."""
    root_url = "https://jsonplaceholder.typicode.com/"
    users_url = f"{root_url}users/{user_id}"
    todos_url = f"{root_url}todos?userId={user_id}"

    try:
        username = requests.get(users_url).json()['username']
        tasks = requests.get(todos_url).json()
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return
    except KeyError:
        print("Failed to retrieve data. User may not exist.")
        return

    tasks_data = [
        {'task': task['title'], 'completed': task['completed'],
            'username': username}
        for task in tasks
    ]

    save_tasks_to_file(user_id, tasks_data)


def save_tasks_to_file(user_id, tasks_data):
    """Save tasks data to a JSON file."""
    filename = f"{user_id}.json"
    with open(filename, "w") as file:
        json.dump({str(user_id): tasks_data}, file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            user_id = int(sys.argv[1])
            fetch_user_tasks(user_id)
        except ValueError:
            print("Please provide a valid integer for the user ID.")
    else:
        print("Usage: ./2-export_to_JSON.py <user_id>")
