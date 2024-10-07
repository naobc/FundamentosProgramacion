# Función para calcular el perímetro y área de un rectángulo
def calcular_rectangulo(base, altura):
    # Cálculo del perímetro
    perimetro = 2 * (base + altura)
    
    # Cálculo del área
    area = base * altura
    
    return perimetro, area

# Datos del rectángulo
base = float(input("Introduce la base del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))

# Cálculo
perimetro, area = calcular_rectangulo(base, altura)

# Resultados
print(f"El perímetro del rectángulo es: {perimetro}")
print(f"El área del rectángulo es: {area}")
