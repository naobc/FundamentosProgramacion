# Solicitar al usuario que ingrese una cantidad de minutos
minutos = int(input("Introduce una cantidad de minutos: "))

# Calcular horas y minutos
horas = minutos // 60  # División entera para obtener las horas
minutos_restantes = minutos % 60  # El resto son los minutos

# Mostrar el resultado
print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")
