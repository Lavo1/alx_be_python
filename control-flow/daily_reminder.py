# daily_reminder.py
# Prompt for a Single Task
task = input("Enter your task: ")
time_bound = input("Is this task time-bound? (yes or no): ").lower()
priority = input("Enter the task's priority (high, medium, low): ").lower()
# Process the Task Based on Priority and Time Sensitivity
reminder = ""
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority."
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
# Provide a Customized Reminder
print(reminder)
