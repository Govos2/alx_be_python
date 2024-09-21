task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        reminder = f"Task: {task} is a high priority."
    case "medium":
        reminder = f"Task: {task} is a medium priority."
    case "low":
        reminder = f"Task: {task} is a low priority."
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."
print(reminder)
