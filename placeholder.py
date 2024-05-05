import calendar

def dias_do_mes_ano(ano, mes):
    calendario = calendar.Calendar()
    dias_do_mes = calendario.itermonthdays2(ano, mes)
    lista_dias_semana = [calendar.day_name[dia_semana] for dia_semana in range(7)]

    dias_com_dia_semana = []
    for dia, dia_semana in dias_do_mes:
        if dia != 0:
            dias_com_dia_semana.append([dia, lista_dias_semana[dia_semana]])

    return dias_com_dia_semana

ano = 2024
mes = 5
dias = dias_do_mes_ano(ano, mes)
for dia in dias:
    print(dia)
