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
POSTGRES_SCHEMA = "\"ShopScanner_Schema\""

mydb = psycopg2.connect(
    POSTGRES_URL
)

def borrarBdd():
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM  "+POSTGRES_SCHEMA+".products WHERE id like '%'")
    print("[SISTEMA] Base de datos vaciada")

def guardarProducto(Producto):
    mycursor = mydb.cursor()
    sql = "INSERT INTO "+POSTGRES_SCHEMA+".products (id, name, price, seller, sale, url, image) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Producto.id, (" "+Producto.nombre), Producto.precio, Producto.supermercado, Producto.oferta, Producto.URL, Producto.imagen)
    mycursor.execute(sql, val)
    mydb.commit()
    print('[SISTEMA] producto guardado:    ' + Producto.nombre + '  :  ' + Producto.precio + '  :  ' + Producto.URL + '  :  ' + Producto.imagen + '  :  ' + Producto.oferta + '  :  ' + Producto.supermercado)
