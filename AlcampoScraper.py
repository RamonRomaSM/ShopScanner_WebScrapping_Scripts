import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

import AccesoBdd
from Producto import Producto


browser2 = webdriver.Chrome()
def hacerPeticion(peticion):

    browser2.get(peticion)

    productJson = browser2.find_element(By.XPATH, '/html/body/pre')
    parseJsonIntoProducto(productJson.text)



def parseJsonIntoProducto (jsonAct):

    y = json.loads(jsonAct)
    print(jsonAct)

    for x in range(0, len(y["products"])):
        nombre = y["products"][x]["name"]
        precio = y["products"][x]["price"]["current"]["amount"]
        imagen = y["products"][x]["image"]["src"]
        supermercado = "alcampo"
        nomUrl= str(y["products"][x]["name"]).replace(' ','-')
        URL = "https://www.compraonline.alcampo.es/products/" + nomUrl + "/" + y["products"][x][
            "retailerProductId"]  # https://www.compraonline.alcampo.es/products/ 'name' / 'retailerProductId'
        oferta = 'NONE'

        # para el tema de las ofertas, si hay una etiqueta de oferta en el json, ademas contendra la descripcion de esta, y el id
        # si no no habra etiqueta oferta

        try:
            oferta = y["products"][x]["offers"][0][
                "description"]  # "offers":[{"id":"30e0c5fb-6b10-42bd-9d17-9e4defc88427","retailerPromotionId":"597072_1","description":"Club Alcampo 25% dto acumulado en tu tarjeta","type":"LOYALTY","presentationMode":"DEFAULT"}],"offer":{"id":"30e0c5fb-6b10-42bd-9d17-9e4defc88427","description":"Club Alcampo 25% dto acumulado en tu tarjeta","type":"LOYALTY","retailerPromotionId":"597072_1","presentationMode":"DEFAULT"},"size":{"value":"260g"},"featured":"false"}],"missedPromotions":[]}
        except:
            oferta = 'NONE'

        params = {'nombre': nombre, 'precio': precio, 'imagen': imagen, 'supermercado': supermercado, 'URL': URL, 'oferta': oferta}

        #prod = Producto(nombre,precio,imagen,supermercado,URL,oferta)
        prod = Producto(nombre,precio,imagen,supermercado,URL,oferta)
        prod.guardarEnBdd()




def startScraping () :
    browser = webdriver.Chrome()
    browser.get('https://www.compraonline.alcampo.es/categories')

    time.sleep(1)
    elements = browser.find_elements(By.CSS_SELECTOR, "#product-page > div > div > div.Col-sc-1ia5hrt-0.ijpbiH > div > div > div")
    ids = []
    for element in elements:

        id=element.get_attribute("data-visibility-id")
        if str(id) != "None":
            ids.append(id)

    browser.close()
    #peticion:
    #www.compraonline.alcampo.es/api/v5/products/decorate?productIds=cddc46c1-7884-4a66-a7f6-ae2533188415,aaa39a2d-7f5b-4627-a92e-6b0950331b72
    #ids mide 300 una vez lleno (pero podria cambiar)
    peticion = 'https://www.compraonline.alcampo.es/api/v5/products/decorate?productIds='

    num=31     # numero de productos por peticion
    act=0      # ultimo producto para consultar

    peticionAct = 'https://www.compraonline.alcampo.es/api/v5/products/decorate?productIds='

    while act < len(ids):
        if (act+num) < len(ids):

            for x in range(0 , num):
                peticionAct = peticionAct + ids[act]

                peticionAct = peticionAct + ','
                act=act+1

            print(str("[PETICION ACT] "+peticionAct))
            hacerPeticion(peticionAct) # Hago la peticion

            peticionAct = 'https://www.compraonline.alcampo.es/api/v5/products/decorate?productIds='   #reinicio la peticion

        else:
            peticionAct = peticionAct + ids[act]
            act = act+1
            if x != (len(ids) - 1):
                peticionAct = peticionAct + ','

            if(act == len(ids)):
                print(str("[PETICION ACT] " + peticionAct))
                hacerPeticion(peticionAct) # Hago la peticion
    browser2.close()


