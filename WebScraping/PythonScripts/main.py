import AlcampoScraper
import AccesoBdd
import MercadonaScraper

AccesoBdd.borrarBdd()
AlcampoScraper.startScraping()
MercadonaScraper.startScraping()
print('[SISTEMA] Base de datos actualizada')