task = input("Enter task  your for today:").lower()
priority = input("What is the priority of the task? (high/medium/low): ").lower()
time_bound = input("Is the task time-sensitive? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"The task '{task}' is of high priority."
    case "medium":
        reminder = f"The task '{task}' is of  medium priority."
    case "low":
        reminder = f"The task '{task}' is of low priority."
    case _:
        reminder = f"The task '{task}'  priority is unknown."
if time_bound == "yes":
    print(f"{reminder} that requires immediate attention today!")
elif time_bound == "no":
    print(f"{reminder} Consider completing it when you have free time.")
else:
    print("invalid input")
    
    
       
           
     
           
                 
            
            
    