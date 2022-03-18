from node import Node

class Hash:
    def __init__( self ):
        self.data = []
        self.capacidad = 5
        for i in range( 0, self.capacidad + 1 ):
            self.data.append( None )
    #Cynthia Data[0] ->Cynthia.next = None
    #Vale INDICE -> 0
    #nuevoNodo = Vale

    #aux = Cynthia
    #Cynthia.next = Vale

    #Juan
    #nuevoNodo = Juan
    #indice = 0
    #aux = Cynthia
    #aux = Cynthia.next -> Vale
    #Vale.next = Juan

    #data[0] = Cynthia Cynthia.next=Vale; Vale Vale.next= Juan; Juan

    def agrega( self, nuevoNodo ):
        #Quiero guardar el num 10
        indice = int(int((nuevoNodo.identificador * 13 + 7) / 3) * 11 / 5 ) % self.capacidad #regresa un número entre 0 y mi capacidad
        #Agregar el nodo en DATA
        if self.data[indice] == None:
            self.data[indice] = nuevoNodo
            print("El nodo de ",nuevoNodo.nombre, " se guardará en el índice ", indice)
        else:
            aux = self.data[indice]
            while aux.next != None:
                aux = aux.next
            aux.next = nuevoNodo
            print("El nodo de ", nuevoNodo.nombre, " se agregó en el índice ",indice,". Junto a ",aux.nombre)
        
    def buscaElemento( self, num ):
        #recibo el 13
        indice = int(int((num * 13 + 7) / 3) * 11 / 5 ) % self.capacidad
        #Buscar el nodo!
        if self.data[indice] == None:
            print("El número que ingresaron NO se encuentra en mi tabla de hash")
        else:
            print("El número ", num, " se encuentra en el índice ",indice)
        