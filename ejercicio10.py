# Entradas: calificaciones parciales, examen final, trabajo final
parcial1 = float(input("Ingresa la calificación del primer parcial: "))
parcial2 = float(input("Ingresa la calificación del segundo parcial: "))
parcial3 = float(input("Ingresa la calificación del tercer parcial: "))
examen_final = float(input("Ingresa la calificación del examen final: "))
trabajo_final = float(input("Ingresa la calificación del trabajo final: "))

# Cálculo del promedio de los tres parciales
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

# Cálculo de la calificación final
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

# Salida: calificación final
print(f"La calificación final del alumno es: {calificacion_final:.2f}")
