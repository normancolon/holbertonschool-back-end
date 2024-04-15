import json
import sys


def fetch_data(user_id):

    users = [
        {"id": 1, "username": "Antonette"},
        {"id": 2, "username": "Bret"},
        # Add more users as necessary
    ]
    tasks = [
        {"userId": 1, "title": "Task 1 for user 1", "completed": True},
        {"userId": 2, "title": "Task 1 for user 2", "completed": False},
        {"userId": 2, "title": "Task 2 for user 2", "completed": True},
        # Add more tasks as necessary
    ]

    # Filter user by ID
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return None, None

    # Filter tasks for this user
    user_tasks = [task for task in tasks if task['userId'] == user_id]

    return user, user_tasks


def export_to_json(user_id):
    user, user_tasks = fetch_data(user_id)

    if not user or not user_tasks:
        print(f"No data found for user ID {user_id}")
        return

    # Format data as per the requirements
    output_data = {
        str(user_id): [
            {"task": task["title"], "completed": task["completed"],
                "username": user["username"]}
            for task in user_tasks
        ]
    }

    # Write data to JSON file
    with open(f"{user_id}.json", 'w') as file:
        json.dump(output_data, file, indent=2)

    print(f"Data for user ID {user_id} has been written to {user_id}.json")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <user_id>")
    else:
        try:
            user_id = int(sys.argv[1])
            export_to_json(user_id)
        except ValueError:
            print("Please provide a valid user ID.")
