# daily_reminder.py

# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case to handle different priorities
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be done sometime today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to work on it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task, but it's time-sensitive. Try to fit it in today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
