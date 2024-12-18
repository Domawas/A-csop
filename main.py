import ertekel
import sorozat
import poggyasz
from poggyasz import Poggyasz


lista = poggyasz.beolvasas("csomag.txt")
poggyasz.poggyaszok(lista)
poggyasz.atlag_tomeg(lista)
poggyasz.legmagasabb_poggyasz(lista)