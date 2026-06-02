from datetime import datetime

def validate_task_title(title):
    # None
    if not title or len(title.strip()) == 0:
        print("Error: Task title cannot be empty.")
        return False
    if len(title) < 3:
        print("Error: Task title must be at least 3 characters long.")
        return False
    return True
    
def validate_task_description(description):
    # None    
    if not description or len(description.strip()) == 0:
        print("Error: Task description cannot be empty.")
        return False  
    if len(description) < 5:
        print("Error: Task description must be at least 5 characters long.")
        return False  
    return True
    
def validate_due_date(due_date):
    # None
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        if due_date_obj < datetime.now():
            print("Error: Due date cannot be in the past.")
            return False
        return True
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return False