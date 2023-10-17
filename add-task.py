import requests

# Define task data for the three tasks
tasks = [
    {
        "name": "Buy groceries",
        "description": "Pringles, Snickers, Capsicum, Onion",
        "deadline": "2023-10-20",
        "reminder_time": "2023-10-20T08:00:00",
        "status": "Pending",
        "priority": "Medium"
    },
    {
        "name": "Study",
        "description": "Physics, EVS",
        "deadline": "2023-10-18",
        "reminder_time": "2023-10-17T17:00:00",
        "status": "Pending",
        "priority": "High"
    },
    {
        "name": "Meet friends",
        "description": "At Pheonix Velachery",
        "deadline": "2023-10-22",
        "reminder_time": "2023-10-21T21:00:00",
        "status": "Pending",
        "priority": "Low"
    }
]

# Send POST requests to add the tasks
for task in tasks:
    response = requests.post('http://127.0.0.1:5000/add-task', json=task)

    if response.status_code == 200:
        print(f"Task added successfully: {task['name']}")
    else:
        print(f"Failed to add the task: {task['name']}")
