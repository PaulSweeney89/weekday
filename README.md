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
- To output the
- 


Reference
[Datetime Module](https://www.programiz.com/python-programming/datetime)
[Python Library - Datetime](https://docs.python.org/3/library/datetime.html)
[Real Python - Object Oriented Programmning](https://realpython.com/python3-object-oriented-programming/)

