# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
date = input()
month, day, year = (int(i) for i in date.split(' '))
dayNumber = calendar.weekday(year, month, day)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[dayNumber].upper())