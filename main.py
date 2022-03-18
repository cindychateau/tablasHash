from Hash import Hash

tablaNumeros = Hash()

tablaNumeros.agrega( 13 )
tablaNumeros.agrega( 72 ) #25 por lo pronto no se guarda
tablaNumeros.agrega( 91 ) #100 NO se guarda
tablaNumeros.agrega( 8 )
tablaNumeros.agrega( 10 )

# data[0] = 72
# data[1] = 91
# data[2] = 13
# data[3] = None
# data[4] = 10

print("---------")

tablaNumeros.buscaElemento( 13 )
tablaNumeros.buscaElemento( 10 ) 
tablaNumeros.buscaElemento( 91 ) 
tablaNumeros.buscaElemento( 2 )