task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is this task time-sensitive? (yes or no): ").lower()
match priority:
    case "high":
        reminder = f"Task: {task} is high priority."
    case "medium":
        reminder = f"Task: {task} is medium priority."
    case "low":
        reminder = f"Task: {task} is low priority."
    case _:
        reminder = f"Task: {task} has an unknown priority level."
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
print(reminder)
