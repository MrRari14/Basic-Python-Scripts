# COSTO = horas * costo_por_hora
hours = input("Hi there, please tell me how many hours you´ve worked: ")
hours = float(hours)
rate_per_hour = float(input("Now, please tell me your rate per hour: "))


if hours <= 40:
    costo = hours * rate_per_hour
    print(costo)

elif hours > 40:
    # COSTO = COSTO_BASE + COSTO_ADICIONAL
    # COSTO BASE
    costo_base = 40 * rate_per_hour
    # COSTO ADICIONAL
    # 50 -> 10  --- 40 - 50 = -10
    # 60 -> 20  --- 40 - 60 = -20
    # 110 -> 70 --- 40 - 110 = -70
    # rate_per_hour + rate_per_hour * 0.5
    #                   HOURS      *    COST_PER_HOUR
    costo_adicional = (hours - 40) * (rate_per_hour * 1.5)
    costo = costo_base + costo_adicional
    print(costo)
