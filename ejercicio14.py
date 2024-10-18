# Pedir al usuario que ingrese un número de dos cifras
numero = int(input("Ingresa un número de dos cifras: "))

# Verificar que el número tenga dos cifras
if 10 <= abs(numero) <= 99:
    # Separar las decenas y las unidades
    decenas = numero // 10
    unidades = numero % 10
    
    # Invertir el número
    numero_invertido = (unidades * 10) + decenas
    
    # Mostrar el número invertido
    print(f"El número invertido es: {numero_invertido}")
else:
    print("Por favor ingresa un número de dos cifras.")
