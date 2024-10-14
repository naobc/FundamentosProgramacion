# Solicitar al usuario el sueldo base del vendedor
sueldo_base = float(input("Introduce el sueldo base del vendedor: "))

# Solicitar al usuario los montos de las tres ventas realizadas
venta1 = float(input("Introduce el monto de la primera venta: "))
venta2 = float(input("Introduce el monto de la segunda venta: "))
venta3 = float(input("Introduce el monto de la tercera venta: "))

# Calcular la comisión total (10% sobre las ventas)
comision = (venta1 + venta2 + venta3) * 0.10

# Calcular el sueldo total (sueldo base + comisiones)
sueldo_total = sueldo_base + comision

# Mostrar el resultado
print(f"El total de comisiones por las tres ventas es: ${comision:.2f}")
print(f"El sueldo total que recibirá en el mes es: ${sueldo_total:.2f}")
