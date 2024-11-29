import csv
from sentiment_analyzer import analyze_sentiment

tasks = []

def add_task(name, description=""):
    """Add a task to the list."""
    sentiment = analyze_sentiment(description)
    priority = "High" if sentiment == "negative" else "Low"
    tasks.append({"name": name, "description": description, "priority": priority})
    print(f"Task '{name}' added with priority: {priority}")

def delete_task(name):
    """Delete a task from the list."""
    global tasks
    tasks = [task for task in tasks if task["name"] != name]
    print(f"Task '{name}' removed!")

def display_tasks():
    """Display all tasks sorted by priority."""
    high_priority = [task for task in tasks if task["priority"] == "High"]
    low_priority = [task for task in tasks if task["priority"] == "Low"]

    print("\nHigh Priority Tasks:")
    for task in high_priority:
        print(f"  - {task['name']}: {task['description']}")

    print("\nLow Priority Tasks:")
    for task in low_priority:
        print(f"  - {task['name']}: {task['description']}")

def load_tasks_from_csv(file_path):
    """Load tasks from a CSV file."""
    try:
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                add_task(row["Task Name"], row["Description"])
        print(f"Tasks loaded from {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except KeyError:
        print("Invalid CSV format. Ensure the file has 'Task Name' and 'Description' columns.")
