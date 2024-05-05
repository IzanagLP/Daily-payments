import calendar

#An object is created to me used in other methods.  
calendario = calendar.Calendar()
dias_do_mes = calendario.itermonthdays2(2024, 4)
print(list(dias_do_mes))