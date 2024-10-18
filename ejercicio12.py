import math

# Pedir al usuario las coordenadas del primer punto (x1, y1)
x1 = float(input("Ingresa la coordenada x1: "))
y1 = float(input("Ingresa la coordenada y1: "))

# Pedir al usuario las coordenadas del segundo punto (x2, y2)
x2 = float(input("Ingresa la coordenada x2: "))
y2 = float(input("Ingresa la coordenada y2: "))

# Calcular la distancia entre los dos puntos usando la fórmula
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mostrar el resultado
print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia:.2f}")
