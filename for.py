# for i in range (10):
#     print (i)
# print ("fin")
# for i in range (5,10):
#     print (i)
# print ("fin")

##-------------------------------------------

# numeros =  [1,2,3,4,5,6,7,8,9,10 ]
# for i in numeros:
#     if i % 2 == 0:
#      print (f"{i} es par") 
##-------------------------------

# cadena = "bienvenido a python, estoy aprendiendo a programar"
# vocales = "a,e,i,o,u"
# contador = 0
# for letra in cadena:
#     if letra in vocales:
#         contador += 1
# print (f"el numero de vocales de la cadena son:{contador}")      

# numero = int(input("por favor ingrese un numero entero"))
# for i in range (1,11):
#     print (numero,"x",i,"=", numero*i)

fila = int(input("ingrese numero de filas"))

for i in range (1, fila, +1):
    for j in range (i):
        print ("*", end= "")

