# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Initialize the reminder variable
reminder = ""

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"'{task}' is a high priority task. Consider completing it when you have free time."
    case "medium":
        if time_bound == "yes":
            reminder = f"'{task}' is a medium priority task that requires attention today."
        else:
            reminder = f"'{task}' is a medium priority task. Consider completing it when you have free time."
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority task that requires attention today."
        else:
            reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        print("Error: Invalid priority level.")

# Print the reminder
print("Reminder:", reminder)
