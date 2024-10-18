import math

# Pedir al usuario que ingrese un número
numero = float(input("Ingresa un número: "))

# Calcular la raíz cuadrada
raiz_cuadrada = math.sqrt(numero)

# Calcular la raíz cúbica
raiz_cubica = numero ** (1/3)

# Mostrar los resultados
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada:.2f}")
print(f"La raíz cúbica de {numero} es: {raiz_cubica:.2f}")
