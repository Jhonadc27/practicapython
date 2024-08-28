# //Un estacionamiento requiere determinar el cobro 
# 	//que debe aplicar a las personas que lo utilizan. 
# 	//Considere que el cobro es con base en las horas 
# 	//que lo disponen y que las fracciones de hora se 
# 	//toman como completas. realice el
# 	//código que representen el algoritmo
# 	//que permita determinar el cobro

horas = float(input("ingrese el numero de horas que utilizo el estacionamiento"))
horascompletas = int(horas) + 1 if horas % 1 !=0 else int (horas)
tarifahora= 1000
costototal= horascompletas * tarifahora

print (f"el costo total es:{costototal} ")

