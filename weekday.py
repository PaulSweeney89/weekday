# week 5 task
# program that outputs the day of the week
# and outputs a message based on the day of the week

# import datetime module
import datetime 

# use the now() method of the datetime class for the current date & time
now = datetime.datetime.now()

# use weekday() method to return day of the week
# 0 = Monday ..... 7 = Sunday
weekday = now.weekday()

# updated to tuple for the days of the week; more efficent than using a dictionary (feedback from Andrew)
days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# print day of the week in text
print("Today is", days_of_the_week[weekday])

# if statement to returning weekday string (Monday to Friday)
if weekday in range(0,4):
    print("Yes, unfortunately today is a weekday.")

# else statement to return weekend statement (Saturday & Sunday)
else:
    print("It is the weekend, yay!")
