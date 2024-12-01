import AlcampoScraper
import AccesoBdd
import MercadonaScraper

AccesoBdd.borrarBdd()
AlcampoScraper.startScraping() #Alcampo ha actualizado su API, asi que por ahora esta parte del scraper no funciona
MercadonaScraper.startScraping()
print('[SISTEMA] Base de datos actualizada')