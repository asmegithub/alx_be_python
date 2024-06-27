task=input("What would you like me to remind you about? ")
priority=input("What is the priority of this task? (high, medium, low) ")
time_bounded=input("Is this time bounded? (yes, no) ")
match time_bounded:
    case "yes":
        if(priority=="high"):
            print(f"Reminder: {task}! is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task}! is a low priority task that requires immediate attention today! ")
    case "no":
        if(priority=='high'):
            print(f"Reminder: {task}! is a high priority task Consider completing it when you have free time.")
        else:
            print(f"Note: {task}! is a low priority task Consider completing it when you have free time.")