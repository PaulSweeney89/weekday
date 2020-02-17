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

# dictonary for the days of the week
days_of_the_week = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}

# print day of the week in text
print("Today is", days_of_the_week[weekday])

# if statement to returning weekday string (Monday to Friday)
if weekday in range(0,4):
    print("Yes, unfortunately today is a weekday.")

# else statement to return weekend statement (Saturday & Sunday)
else:
    print("It is the weekend, yay!")
