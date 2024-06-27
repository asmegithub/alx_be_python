task = input("Enter your task: ")
time_bounded = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

match time_bounded:
    case "yes":
        if priority == "high":
            print(f"Reminder: {task}! is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task}! is a low priority task that requires immediate attention today!")
    case "no":
        if priority == "high":
            print(f"Reminder: {task}! is a high priority task. Consider completing it when you have free time.")
        else:
            print(f"Note: {task}! is a low priority task. Consider completing it when you have free time.")
