num = int(input("ingrese un numero"))
if num >= 0:
    x = 1
    f = 1
    while x <= num:
        f = f * x
        x += 1 
    print ("el factorial de ", num, "es:", f)
else:
    print ("no se puede calcular el factorial")     