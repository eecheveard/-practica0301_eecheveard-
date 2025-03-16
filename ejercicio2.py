import csv
import cProfile

# Función para poner el nombre en formato capitalizado
def capitalizar_nombre(nombre):
    return nombre.title()

# Función para calcular la letra del DNI
def calcular_letra_dni(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[dni % 23]