"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

# Entradas
text = input("Ingresa una palabra: ")

# Proceso
texto = text.strip()  # Elimina espacios en blanco al inicio y al final
if texto== "":
    print("No ingresaste ninguna palabra")
else:
    if texto[0] in vocales:
        salida ="La palabra comienza con una vocal"
    else:
        salida ="La palabra no comienza con una vocal"

# Salidas
print(salida)
