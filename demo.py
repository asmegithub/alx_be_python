from datetime import *

current_date = datetime.now()
print(
    "Current date and time:",
    current_date.strftime("%Y-%m-%d %H:%M:%S"),
)
number_of_days = int(input("Enter the number of days to add to the current date:"))
future_date = datetime.now() + timedelta(days=number_of_days)
print(future_date.strftime("%Y-%m-%d"))
