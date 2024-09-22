Task = input("Enter task  your for today:")
Priority = input("What is the priority of the task? (high/medium/low): ")
Time_bound = input("Is the task time-sensitive? (yes/no): ")

match Priority:
    case "high":
        reminder = f"The task '{task}' is of high priority."
    case "medium":
        reminder = f"The task '{task}' is of  medium priority."
    case "low":
        reminder = f"The task '{task}' is of low priority."
    case _:
        reminder = f"The task '{task}'  priority is unknown."
        if Time_bound == "yes":
            reminder += "task requires immediate attention today!"
print(reminder)            
     
           
                 
            
            
    