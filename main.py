from ManejadorFlores import ManejadorFlores
from ManejadorRamos import ManejadorRamos
from Menu import Menu


if __name__=='__main__':
   
    unManejadorRamos = ManejadorRamos()
    unManejadorFlores = ManejadorFlores()
    unMenu = Menu()
    unManejadorFlores.cargarCSV("flores.csv")
    unMenu.ejecutarMenu(unManejadorRamos, unManejadorFlores)