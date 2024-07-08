import datetime

num_days = int(input("Enter the number of days: "))
future_date = datetime.datetime.now() + datetime.timedelta(days=num_days)
print(future_date.strftime("%Y-%m-%d"))
