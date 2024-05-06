import calendar

def main():
    def find_month_by_number(month: int) -> str:
        """
        :receive: A number between 1-12.
        :return: The respective month related to the number.
        """
        month_names = list(calendar.month_name)
        month_numbers = list(range(13))
        numered_months_list = list(zip(month_numbers, month_names))
        return numered_months_list[month][1]

    #This function receives year and month as parameters to return how much money is made on the month.
    def payments(year: int, month: int) -> int:
        calendar_class = calendar.TextCalendar(calendar.MONDAY)
        #Creates an list with tuples of day number + week day number(1-7).
        days_month = []
        for day_number in calendar_class.itermonthdays2(year, month):
            days_month.append(day_number)

        #Creates a list of strings with the days of the week.
        days_names = []
        for name in calendar.day_name:
            days_names.append(name)

        #Creates a list with the days numbers + day of the week name
        list_day_number_plus_day_name = []
        for day, day_name in days_month:
            if day != 0:
                list_day_number_plus_day_name.append([day, days_names[day_name]])

        #Starts a counter with the days worked and increases it's value for each time the loop passes for a week day that is not Tuesday
        days_worked = 0
        for day_number, day_name in list_day_number_plus_day_name:
            if day_name != "Tuesday":
                days_worked += 1

        salary = days_worked * 100

        #Returns the result of the work day payment * days worked
        return salary

    def results(month: int) -> None:
        print(f'On the month of {find_month_by_number(month)} you will receive R${payments(2024, month)}.')

    while True:
        try:
            month = int(input("Input the month number: "))
            if month in range(13):
                results(month)
                break
        except ValueError:
            print("Insert a valid number.")
if __name__ == "__main__":
   main()