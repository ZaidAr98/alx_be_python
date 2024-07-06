from datetime import *
def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date)


def calculate_future_date(future_date):
    current_date = datetime.now()
    time_delta = timedelta(days=future_date)
    future_date = current_date + time_delta
    print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))






display_current_datetime()
future_date =  int(input("Enter the number of days to add to the current date: "))
calculate_future_date(future_date)