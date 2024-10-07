'''
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa
'''
import math

# Función para calcular la hipotenusa
def calcular_hipotenusa(cateto1, cateto2):
    # Usamos el teorema de Pitágoras: hipotenusa = sqrt(cateto1^2 + cateto2^2)
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    return hipotenusa

# Datos del triángulo
cateto1 = float(input("Introduce el primer cateto: "))
cateto2 = float(input("Introduce el segundo cateto: "))

# Cálculo
hipotenusa = calcular_hipotenusa(cateto1, cateto2)

# Resultados
print(f"La hipotenusa del triángulo es: {hipotenusa}")
