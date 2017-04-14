import sys
sys.path.insert(0, './lib')
import dit_data
import dit_menu
import dit_price
import dit_airports
import dit_planes




# this is main class. Keeps everything inside
class ditFlight():
  
  def __init__(self):
    __data = dit_data.ditData()
    #self.planesArray = __data.getArrayOfPlanes()
    # self.airportsArray = __data.getArrayOfAirports()
    self.planes = dit_planes.Planes(__data.getArrayOfPlanes())
    self.airports = dit_airports.Airports(__data.getArrayOfAirports())
    self.currencyArray = __data.getArrayOfCurrency()
    self.countryCurrency = __data.getArrayOfcountryCurrency()
    self.price = dit_price.Price(self)
    self.menu = dit_menu.Menu(self)




  # def showAirportTable(self):
  #   x = prettytable.PrettyTable(["ID","NAME","CITY","COUNTRY","CODE"])
  #   for row in self.airportsArray:
  #     x.add_row([row[0], row[1][:20], row[2][:15], row[3][:13], row[4][:5]])
  #   print (x)    


  # def showCurrencyArray(self):
  #   x = prettytable.PrettyTable(['NAME','CODE','RATE1','RATE2'])
  #   for row in self.currencyArray:
  #     x.add_row(row)
  #   print (x)

#name,name_fr,ISO3166-1-Alpha-2,ISO3166-1-Alpha-3,ISO3166-1-numeric,ITU,MARC,WMO,DS,Dial,FIFA,FIPS,GAUL,IOC,currency_alphabetic_code,currency_country_name,cu
#Poland     ,Pologne,       PL, POL, 616, POL, pl,PL,PL,48,POL,PL,198,POL,PLN,POLAND,2,Zloty,985,Yes
#South Sudan,Soudan du Sud, SS, SSD, 728, SSD, sd,,,211,,OD,,,SSP,SOUTH SUDAN,2,South Sudanese Pound,728,Yes

  def showCountryCurrencyTable(self):
    #print ("showCountryCurrencyTable")
    x = prettytable.PrettyTable(["COUNTRY","CODE", "NAME","SYMBOL"])
    ignore_first_row = True
    for row in self.countryCurrency:
      if (ignore_first_row):
        ignore_first_row = False
        continue
      x.add_row( [row[0][:40], row[2], row[17],row[14] ] )
    print (x)


  # def calculateDistance(airport1, airport2):
  #   return 'not yet ready'
