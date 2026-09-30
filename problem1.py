import datetime

current_datetime = datetime.datetime.now()
datetime_str =  current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print("Current Date and Time:", datetime_str)