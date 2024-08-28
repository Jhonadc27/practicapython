# Escribe un programa en Python que solicite al usuario ingresar una lista de números enteros. Luego,
#  el programa debe calcular e imprimir la suma de todos los números ingresados. El programa debe continuar
#  solicitando números hasta que el usuario decida dejar de ingresar más.

# Requisitos:

# El programa debe permitir al usuario ingresar números uno por uno.
# Después de ingresar cada número, el usuario debe ser preguntado si desea agregar otro número.
# Si el usuario decide que no quiere agregar más números, el programa debe calcular y mostrar la suma total 
# de los números ingresados.

numeros = []
while True:
    try:
     numeros = int(input("ingrese un numero entero:" ))  
     numeros.append(numero)
     continue = input ("desea agregar otro numero (s/n):")
      if continue.lower
       break
    suma_total = sum (numeros)
    print (f"/nLa suma total de los numeros ingresados es:¨{suma_total}")