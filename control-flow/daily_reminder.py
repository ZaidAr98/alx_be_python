task  = str(input("Enter your task: "))
Priority  = str(input("Priority (high/medium/low): "))
time = str(input("Is it time-bound? (yes/no): "))


match Priority :
    case "high":
         if time == "yes" :
           print(f"Reminder: {task} is a {Priority} priority task that requires immediate attention today!")
         elif time == "no":
            print(f"Note: {task} is a {Priority} priority task. Consider completing it when you have free time")

    case "medium":
         if time == "yes" :
           print(f"Reminder: {task} is a {Priority} priority task that requires immediate attention today!")
         elif time == "no":
            print(f"Note: {task} is a {Priority} priority task. Consider completing it when you have free time")        

    case "low":
         if time == "yes" :
           print(f"Reminder: {task} is a {Priority} priority task that requires immediate attention today!")
         elif time == "no":
            print(f"Note: {task} is a {Priority} priority task. Consider completing it when you have free time")