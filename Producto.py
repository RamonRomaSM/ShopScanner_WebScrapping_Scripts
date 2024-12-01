import AccesoBdd


class Producto:
    nombre = ''
    precio = 0
    imagen = ''
    supermercado = ''
    URL = ''
    oferta = '' #si no esta en oferta qui pondra 'no'
    id=''

    def __init__(self,nombre,precio,imagen,supermercado,URL,oferta):
        self.nombre=nombre
        self.URL = str(URL)
        self.precio = str(precio)
        self.oferta = str(oferta)
        self.imagen = str(imagen)
        self.supermercado = str(supermercado)
        self.id = nombre + supermercado + precio + oferta


    def guardarEnBdd(self):
        try:
            AccesoBdd.guardarProducto(self)
        except:
            print("[SISTEMA]: producto duplicado no se guardo: "+self.id)