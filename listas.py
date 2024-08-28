frutas = ["manzana", "pera","uva","banano"] 
frutas.append ("sandia") #para agregar un elemento a la lista
frutas.insert (0, "sandia") #para agregar un elemento en una posicion especifica
frutas.extend (["mango", "kiwi","lulo"]) #para agregar multiples elementos a la lista
frutas [0] = "limon" # para editar un elemento en la lista
frutas.remove ("sandia") # para remover un elemento de la lista

del frutas [7] # para eliminar un elemento de la listacon el numero del elemento
del frutas [2:4] # para eliminar por rangos
frutas.clear ()


frutaeliminada = frutas.pop (1)
print (frutas)
print (frutaeliminada)

# for i in frutas:
#     print (i)