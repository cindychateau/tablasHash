from Hash import Hash
from node import Node

tablaNumeros = Hash()

persona1 = Node("Cynthia", "Castillo", 123)
persona2 = Node("Valeria", "Romero", 456)
persona3 = Node("Juan", "Perez", 789)

tablaNumeros.agrega(persona1)
tablaNumeros.agrega(persona2)
tablaNumeros.agrega(persona3)

# data[0] = 72
# data[1] = 91
# data[2] = 13
# data[3] = None
# data[4] = 10

# print("---------")

# tablaNumeros.buscaElemento( 13 )
# tablaNumeros.buscaElemento( 10 ) 
# tablaNumeros.buscaElemento( 91 ) 
# tablaNumeros.buscaElemento( 2 )