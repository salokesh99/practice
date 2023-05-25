import calendar

# p = list(map(int, input().split()))
p = [5, 23, 2023]


m = p[0]
d = p[1]
y = p[2]
# print(m, d, y)
print(calendar.day_name[calendar.weekday(y,m,d)].upper())

print(list(calendar.day_name))

print(calendar.weekday(y,m,d))

print(calendar.firstweekday())

print(calendar.isleap(2024))
print(calendar.isleap(2023))

v = calendar.setfirstweekday(calendar.SUNDAY)
print(v)

calendar.prmonth(2023, 5)

calendar.setfirstweekday(4)
print(calendar.firstweekday())
calendar.prmonth(2023, 5)


print(calendar.TUESDAY)
print(list(calendar.day_name))
# print(calendar.month(theyear, themonth))

print(calendar.calendar(2023))
calendar.setfirstweekday(6)
print(calendar.calendar(2023))

print(calendar.TextCalendar(firstweekday=6).formatyear(2023))
print(calendar.TextCalendar(firstweekday=0).formatyear(2023))
