import calendar

#Takes the month and print 
march = calendar.TextCalendar(calendar.MONDAY)
days_month = []
for day_number in march.itermonthdays2(2024, 5):
    days_month.append(day_number)

days_names = []
for name in calendar.day_name:
    days_names.append(name)

list_day_number_plus_day_name = []
for day, day_name in days_month:
    if day != 0:
        list_day_number_plus_day_name.append([day, days_names[day_name]])

for day_number in list_day_number_plus_day_name:
    print(day_number)

days_worked_counter = 0
for day_number, day_name in list_day_number_plus_day_name:
    if day_name != "Tuesday":
        days_worked_counter += 1

print(days_worked_counter)