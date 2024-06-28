task  = str(input("Enter your task: "))
Priority  = str(input("Priority (high/medium/low): "))
time_bound = str(input("Is it time-bound? (yes/no): "))

reminder = f"{task} is a {Priority} priority task"
match Priority :
    case "high":
              reminder = f"{task} is a {Priority} priority task"

    case "medium":
              reminder = f"{task} is a {Priority} priority task"  

    case "low":
              reminder = f"{task} is a {Priority} priority task"  


if(time_bound == "yes"):
     print(f"{reminder} This task requires immediate attention today!")
    