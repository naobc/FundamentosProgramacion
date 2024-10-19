# Solicitar los valores de A y B al usuario
A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))

# Mostrar los valores originales
print(f"Valores originales: A = {A}, B = {B}")

# Intercambiar los valores
A, B = B, A

# Mostrar los valores intercambiados
print(f"Valores después del intercambio: A = {A}, B = {B}")
