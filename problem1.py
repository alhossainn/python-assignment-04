import datetime

current_datetime = datetime.datetime.now()
time_str =  current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print("Current Date and Time:", time_str)