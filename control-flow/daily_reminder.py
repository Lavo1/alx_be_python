# daily_reminder.py
# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder = ""
match priority.lower():
    case "high":
        reminder = f"Reminder: {task} [HIGH priority]."
    case "medium":
        reminder = f"Reminder: {task} [MEDIUM priority]."
    case "low":
        reminder = f"Reminder: {task} [LOW priority]."
    case _:
        reminder = f"Reminder: {task} [UNKNOWN priority]."
if time_bound.lower() == "yes":
    reminder += " That requires immediate attention today!"
print(reminder)

