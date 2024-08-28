nombres = [ "ana","luis","maria", "pedro","sofia" ]
combinaciones = []

for i in range (len(nombres)):
    for j in range (i + 1, len (nombres)):
        combinaciones.append((nombres[i], nombres [j]))

for par in combinaciones:
    print(f"par:{par[0]} y {par[1]}")

print (f"\ntotal de pares unicos generados:{len(combinaciones)}")    