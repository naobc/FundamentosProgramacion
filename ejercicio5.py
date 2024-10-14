# Función para convertir Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Solicitar al usuario que ingrese un valor en Fahrenheit
fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))

# Convertir la temperatura a Celsius
celsius = fahrenheit_a_celsius(fahrenheit)

# Mostrar el resultado
print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.")
