task  = str(input("Enter your task: "))
Priority  = str(input("Priority (high/medium/low): "))
time_bound = str(input("Is it time-bound? (yes/no): "))

match Priority :
    case "high":
              reminder = f"{task} is a {Priority} priority task"

    case "medium":
              reminder = f"{task} is a {Priority} priority task"  

    case "low":
              reminder = f"{task} is a {Priority} priority task"  


if time_bound == "yes":
     print(f"Reminder: {reminder} that requires immediate attention today!")
else :
     print(f"Note: {reminder} Consider completing it when you have free time.")