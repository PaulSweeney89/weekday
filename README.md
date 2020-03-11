# Weekday
**Simple program which ouputs the current day of the week when the program is run and returns a string based on it being a weekday or the weekend.**

*Week 5 Programming &amp; Scripting Task*

Program Overview:

- Program imports the datetime module
```
import datetime
```
- Program uses the .now() method of the datetime class to return the current date and time of when the program is executed and assigns it to the variable now.
```
now = datetime.datetime.now()
```
- Program uses the .weekday() method to return the current day of the week as an interger and assigns it to the variable weekday, where Monday is 0 and Sunday is 6.
```
weekday = now.weekday()
```
- To output the day of the week as text, use a dictonary with the interger values assigned as keys and the values assigned with the equivalent days of the week.
```
days_of_the_week = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
```
- Alternatively use a tuple instead of a dictionary to return the current day of the week, more efficient approach than using a dictionary. 
(Feedback from Andrew 11.03.2020)
```
days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
```
- Output day of the week.
```
print("Today is", days_of_the_week[weekday])
```
- Using an **if** statement, output the string "Yes, unfortunately today is a weekday" when the current day is a weekday, weekday variable value is in the range 0 - 4.
```
if weekday in range(0,4):
    print("Yes, unfortunately today is a weekday.")
```
- Using a **else** statement, output the string "It is the weekend, yay!" when the current day is during the weekend, weekday variable value is either 5 or 6.
```
else:
    print("It is the weekend, yay!")
```

References:

[Datetime Module](https://www.programiz.com/python-programming/datetime)

[Python Library - Datetime](https://docs.python.org/3/library/datetime.html)

[Real Python - Object Oriented Programmning](https://realpython.com/python3-object-oriented-programming/)

