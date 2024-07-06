import datetime
def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date)


def calculate_future_date(future_date):
    current_date = datetime.datetime.now()
    time_delta = datetime.timedelta(days=future_date)
    future_date = current_date + time_delta
    specific_datetime = datetime.datetime.strftime(future_date, "%Y-%m-%d %H:%M:%S")
    print("Future date:", specific_datetime)






display_current_datetime()
future_date =  int(input("Enter the number of days to add to the current date: "))
calculate_future_date(future_date)