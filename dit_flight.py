import sys
sys.path.insert(0, './lib')
import prettytable
import dit_data
import dit_menu

# this is main class. Keeps everything inside
class ditFlight():
  
  def __init__(self):
    __data = dit_data.ditData()
    self.planesArray = __data.getArrayOfPlanes()
    self.airportsArray = __data.getArrayOfAirports()
    self.menu = dit_menu.Menu()


  def showPlanesTable(self):
    x = prettytable.PrettyTable(['CODE','TYPE','UNITS','MANUFACTURER','RANGE','TANK_CAPACITY'])
    for row in self.planesArray:
      x.add_row(row)
    print (x)    


  def showAirportTable(self):
    x = prettytable.PrettyTable(["ID","NAME","CITY","COUNTRY","CODE"])
    for row in self.airportsArray:
      x.add_row([row[0], row[1][:20], row[2][:15], row[3][:13], row[4][:5]])
    print (x)    


  def calculateDistance(airport1, airport2):
    return 'not yet ready'
