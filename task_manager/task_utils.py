from datetime import datetime

# Import validation functions
# None
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        return
    if not validate_task_description(description):
        return
    if not validate_due_date(due_date):
        return
    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if 0 < index >= len(tasks):
        print("Error: Invalid task index.")
        return
        tasks[index]["completed"] = True
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    # None
    found = False
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i}. {task['title']} - Due: {task['due_date']}")
            found = True
    if not found:
        print("No pending tasks.")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    # None
    if len(tasks) == 0:
     print("No tasks available.")
    return 0
    completed = 0 
    for task in tasks:
            if task["completed"]:
                completed += 1

    progress = (completed / len(tasks)) * 100
    print(f"Progress: {progress:.2f}%")
    return progress