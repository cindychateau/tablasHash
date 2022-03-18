class Hash:
    def __init__( self ):
        self.data = []
        self.capacidad = 5
        for i in range( 0, self.capacidad + 1 ):
            self.data.append( None )

    def agrega( self, num ):
        #Quiero guardar el num 10
        indice = int(int((num * 13 + 7) / 3) * 11 / 5 ) % self.capacidad #regresa un número entre 0 y mi capacidad
        #Agregar el nodo en DATA
        if self.data[indice] == None:
            self.data[indice] = num
            print("El número ",num, " se guardará en el índice ", indice)
        else:
            print("El índice ", indice, " para el numero ",num," no está disponible. Hay que ajustar la lista")
        
    def buscaElemento( self, num ):
        #recibo el 13
        indice = int(int((num * 13 + 7) / 3) * 11 / 5 ) % self.capacidad
        #Buscar el nodo!
        if self.data[indice] == None:
            print("El número que ingresaron NO se encuentra en mi tabla de hash")
        else:
            print("El número ", num, " se encuentra en el índice ",indice)
        