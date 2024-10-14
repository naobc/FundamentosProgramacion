# Solicitar al usuario el total de la compra
total_compra = float(input("Introduce el total de la compra: "))

# Calcular el descuento (15% sobre el total de la compra)
descuento = total_compra * 0.15

# Calcular el total a pagar después del descuento
total_final = total_compra - descuento

# Mostrar el resultado
print(f"El descuento es: ${descuento:.2f}")
print(f"El total a pagar después del descuento es: ${total_final:.2f}")
