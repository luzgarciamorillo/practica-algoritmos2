# ---------------------------------------------------
# PRÁCTICA 2 ALGORITMOS: ÁREA DE UN CÍRCULO
# ---------------------------------------------------
import math
# Paso 1: Solicitar al usuario que ingrese el radio del círculo.
radio = float(input("Por favor, ingrese el radio del círculo: "))

# Paso 2: Calcular la fórmula
area = math.pi * (radio**2)

# Paso 3: Mostrar al usuario el área calculada
print("El área del círculo con radio", radio, "es: ", area)