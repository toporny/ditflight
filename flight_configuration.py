import csv
import os.path
import sys
import dit_plane
import dit_airport
sys.path.insert(0, './lib')
sys.path.insert(0, './data_csv')
import prettytable


class Configuration():
  def __init__(self):
    self.currencyrates_file = 'data_csv/currencyrates.csv'
    self.countrycurrency_file = 'data_csv/countrycurrency.csv'
    self.airport_file = 'data_csv/airport.csv'
    self.aircraft_file = 'data_csv/aircraft.csv'
    
    error_array = []
    if (not(os.path.isfile(self.airport_file))):
      error_array.append(self.airport_file +' file does not exist!')
    if (not(os.path.isfile(self.countrycurrency_file))):
      error_array.append(self.countrycurrency_file +' file does not exist!')
    if (not(os.path.isfile(self.currencyrates_file))):
      error_array.append(self.currencyrates_file +' file does not exist!')
    if (not(os.path.isfile(self.aircraft_file))):
      error_array.append(self.aircraft_file +' file ttradoes not exist!')

    if (len(error_array)>0):
      print ("Fatal error occured:")
      for n in error_array:
        print (n)
      sys.exit(-1)
    
      
  def showPlanesTable(self):
    file  = open(self.aircraft_file, "rt", encoding="utf8")
    read = csv.reader(file)
    firstrow = 0
    for row in read:
      firstrow = firstrow + 1
      if (firstrow == 1):
        x = prettytable.PrettyTable(row)
      else:
        x.add_row(row)
    print (x)

    
    
  def getArrayOfPlanes(self):
    file  = open(self.aircraft_file, "rt", encoding="utf8")
    read = csv.reader(file)
    firstrow = 0
    arrayPlanes = []
    for row in read:
      firstrow = firstrow + 1
      if (firstrow == 1):  # pass first line with definition of data
        continue
      plane = dit_plane.Plane(row)
      arrayPlanes.append(plane)
    return (arrayPlanes)
    
  
  def getArrayOfAirports(self):
    file  = open(self.airport_file, "rt", encoding="utf8")
    read = csv.reader(file)
    arrayAirports = []
    for row in read:
      airport = dit_airport.Airport(row)
      arrayAirports.append(airport)
      #print(airport.getAirportName())
    return (arrayAirports)
    
    
    
  
  def showAirportsTable(self):
    file  = open(self.airport_file, "rt", encoding="utf8")
    read = csv.reader(file)
    x = prettytable.PrettyTable(["ID","NAME","CITY","COUNTRY","CODE"])
    for row in read:
      x.add_row([row[0], row[1][:20], row[2][:15], row[3][:13], row[4][:5]])
    print (x)
