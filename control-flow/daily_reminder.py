task  = str(input("Enter your task: "))
Priority  = str(input("Priority (high/medium/low): "))
time_bound = str(input("Is it time-bound? (yes/no): "))

match Priority :
    case "high":
              Reminder = f"{task} is a {Priority} priority task"

    case "medium":
              Reminder = f"{task} is a {Priority} priority task"  

    case "low":
              Reminder = f"{task} is a {Priority} priority task"  


if time_bound == "yes":
     print(f"{Reminder} that requires immediate attention today!")
    