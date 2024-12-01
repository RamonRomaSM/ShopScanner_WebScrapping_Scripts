from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import Producto

from Producto import Producto



def hacerPeticion(peticion):
    browser2 = webdriver.Chrome()

    browser2.get(peticion)
    productJson = browser2.find_element(By.XPATH, '/html/body/pre')
    print(str("[PETICION ACT] " + peticion))
    parseJsonIntoProducto(productJson.text)

    browser2.close()

def parseJsonIntoProducto (jsonAct):

    y = json.loads(jsonAct)
    for x in range(0, len(y["categories"][0]["products"])):
        nombre = y["categories"][0]["products"][x]["display_name"]
        precio = y["categories"][0]["products"][x]["price_instructions"]["unit_price"]
        imagen = y["categories"][0]["products"][x]["thumbnail"]
        supermercado = "mercadona"
        URL = y["categories"][0]["products"][x]["share_url"]
        oferta = y["categories"][0]["products"][x]["price_instructions"]["previous_unit_price"]
        if not oferta:
            oferta = "NONE"


        params = {'nombre': nombre, 'precio': precio, 'imagen': imagen, 'supermercado': supermercado, 'URL': URL,
                  'oferta': oferta}
        prod = Producto(nombre, precio, imagen, supermercado, URL, oferta)
        prod.guardarEnBdd()



def startScraping():
    print("escrapeo")
    #estas son las paginas que llamo de la api,
    paginas = {27, 28, 29, 31, 32, 34, 36, 37, 38, 40, 42, 43, 44, 45, 46, 47, 48, 59, 60, 62, 64, 65, 66, 68, 69, 71, 72, 75, 77, 78, 79, 80, 81, 83, 84, 86, 88, 89, 90, 92, 95, 97, 98, 99, 100, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 120, 121, 122, 126, 127, 129, 130, 132, 133, 135, 138, 140, 142, 143, 145, 147, 148, 149, 150, 151, 152, 154, 155, 158, 159, 161, 162, 163, 164, 166, 168, 169, 170, 171, 173, 174, 181, 789, 884, 897}
    for x in paginas:
        peticion = 'https://tienda.mercadona.es/api/categories/'+str(x)+'/?lang=es&wh=mad1'
        hacerPeticion(peticion)

