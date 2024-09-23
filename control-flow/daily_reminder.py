def reminder():
    try:
        task = input("Enter your task: ").lower()
        priority = input("Priority (high/medium/low): ").lower()
        time_bound = input("Is it time-bound? (yes/no):")
    except ValueError:
        print("Invalid data!, try again")
        return
    match priority:
        case "high":
            priority_message = "is a high priority task"
        case "medium":
            priority_message = "is a medium priority task"
        case "low":
            priority_message = "is a low priority task"
        case _:
            print("invalid data, try again")
            return
    if time_bound == "yes":
        print(f"Reminder: '{task}' {priority_message} that requires immediate attention!")
    elif time_bound == "no":
        print(f"Note: '{task}' {priority_message}. Consider completing it when you have free time")
    else:
        print("Invalid time-bound input, please enter 'yes' or 'no'.")

reminder()