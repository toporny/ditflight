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
    self.currencyArray = __data.getArrayOfCurrency()
    self.countryCurrency = __data.getArrayOfcountryCurrency()


    self.menu = dit_menu.Menu()


    # self.__airport_data = []
    # self.__aircraft_data = []
    # self.__currencyRates = []
    # self.__countryCurrency = []

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

  def showCurrencyArray(self):
    # print ("showCurrencyArray")
    x = prettytable.PrettyTable(['NAME','CODE','RATE1','RATE2'])
    for row in self.currencyArray:
      x.add_row(row)
    print (x)

#name,name_fr,ISO3166-1-Alpha-2,ISO3166-1-Alpha-3,ISO3166-1-numeric,ITU,MARC,WMO,DS,Dial,FIFA,FIPS,GAUL,IOC,currency_alphabetic_code,currency_country_name,cu
#Poland, Pologne,PL,POL,616,POL,pl,PL,PL,48,POL,PL,198,POL,PLN,POLAND,2,Zloty,985,Yes
  def showCountryCurrencyTable(self):
    #print ("showCountryCurrencyTable")
    x = prettytable.PrettyTable(["NAME","CODE", "CURRENCY NAME","COUNTRY"])
    for row in self.countryCurrency:
      x.add_row( [row[0][:20], row[1], row[1], row[1] ] )
    print (x)


  # def calculateDistance(airport1, airport2):
  #   return 'not yet ready'
