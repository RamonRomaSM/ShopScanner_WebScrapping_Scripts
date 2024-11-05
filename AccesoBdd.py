import mysql.connector
import psycopg2

POSTGRES_URL="#"
POSTGRES_PRISMA_URL="#"
POSTGRES_URL_NO_SSL="#"
POSTGRES_URL_NON_POOLING="#"
POSTGRES_USER="#"
POSTGRES_HOST="#"
POSTGRES_PASSWORD="#"
POSTGRES_DATABASE="#"

mydb = psycopg2.connect(
    host=POSTGRES_HOST,
    dbname=POSTGRES_DATABASE,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD
)

"""
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nosequeponer"
)
"""

def borrarBdd():

    mycursor = mydb.cursor()

    mycursor.execute("DELETE FROM productos")
    mycursor.execute("ALTER SEQUENCE productos_num_seq RESTART WITH 1;")
    print("[SISTEMA] Base de datos vaciada")

def guardarProducto(Producto):
    mycursor = mydb.cursor()
    #sql = "INSERT INTO tfg.productos (idproductos, nombre, precio, supermercado, oferta, url, imagen) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    sql = "INSERT INTO productos (idproductos, nombre, precio, supermercado, oferta, url, imagen) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Producto.id, (" "+Producto.nombre), Producto.precio, Producto.supermercado, Producto.oferta, Producto.URL, Producto.imagen)
    mycursor.execute(sql, val)

    mydb.commit()
    print('[SISTEMA] producto guardado:    ' + Producto.nombre + '  :  ' + Producto.precio + '  :  ' + Producto.URL + '  :  ' + Producto.imagen + '  :  ' + Producto.oferta + '  :  ' + Producto.supermercado)