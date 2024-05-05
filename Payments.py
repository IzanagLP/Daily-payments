import calendar

def main():
    def payments(year, month):
        calendar_class = calendar.TextCalendar(calendar.MONDAY)
        
        days_month = []
        for day_number in calendar_class.itermonthdays2(year, month):
            days_month.append(day_number)

        days_names = []
        for name in calendar.day_name:
            days_names.append(name)

        list_day_number_plus_day_name = []
        for day, day_name in days_month:
            if day != 0:
                list_day_number_plus_day_name.append([day, days_names[day_name]])

        days_worked_counter = 0
        for day_number, day_name in list_day_number_plus_day_name:
            if day_name != "Tuesday":
                days_worked_counter += 1
        
        salary = days_worked_counter * 100

        return salary

    year = 2024
    month = int(input("Input the month number: "))
    print(payments(year, month))

if __name__ == "__main__":
   main()