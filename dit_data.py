import csv
import os.path
import sys
sys.path.insert(0, './lib')
sys.path.insert(0, './data_csv')

from colorconsole import terminal


class ditData():

  # constructor

  def __init__(self):

    # initializes all data
    self.__currencyrates_file = 'data_csv/currencyrates.csv'
    self.__countrycurrency_file = 'data_csv/countrycurrency.csv'
    self.__airport_file = 'data_csv/airport.csv'
    self.__aircraft_file = 'data_csv/aircraft.csv'

    self.__airport_data = []
    self.__aircraft_data = []
    self.__currencyRates = []
    self.__countryCurrency = []


    # Checks if all files exist
    error_array = []

    if (not(os.path.isfile(self.__airport_file))):
      error_array.append(self.__airport_file)

    if (not(os.path.isfile(self.__countrycurrency_file))):
      error_array.append(self.__countrycurrency_file)

    if (not(os.path.isfile(self.__currencyrates_file))):
      error_array.append(self.__currencyrates_file)

    if (not(os.path.isfile(self.__aircraft_file))):
      error_array.append(self.__aircraft_file)

    if (len(error_array)>0):
      print ("Fatal error occured:")
      for n in error_array:
        print (n, 'file does not exist!')
      sys.exit(-1)

    # check integrity and gets data from AIRCRAFT csv file
    self.__aircraft_data = self.__getDataFromFile(self.__aircraft_file, 6, True) # True means: "ignore first row"

    # same with AIRCRAFT csv file
    self.__airport_data = self.__getDataFromFile(self.__airport_file, 12)

    # same with CURRENCY csv file
    self.__currencyRates = self.__getDataFromFile(self.__currencyrates_file, 4)

    # same with CURRENCY csv file
    self.__countryCurrency = self.__getDataFromFile(self.__countrycurrency_file, 20)



  # check integrity and gets data from file
  def __getDataFromFile(self, fileName, columns, passFirstLine = False):
    file  = open(fileName, "rt", encoding="utf8")
    read = csv.reader(file)
    __data = []
    rowcount = 0
    for row in read:
      if (passFirstLine == True):
        rowcount = rowcount + 1
      if (rowcount != 1):
        if (len(row) != columns):
          screen = terminal.get_terminal(conEmu=False)
          screen.set_color(terminal.colors["RED"])  # screen.set_color(terminal.colors["WHITE"],terminal.colors["BLUE"])
          print ("file "+ fileName+" error! line "+str(rowcount)+ '. Has to be exactly '+str(columns)+' columns!')
          screen.reset_colors()
          sys.exit(-1)
        __data.append(row)
    file.close() # close file
    return __data

     
  # gets array of planes
  def getArrayOfPlanes(self):
    print(self.__aircraft_data)
    return self.__aircraft_data


  # gets array of airports
  def getArrayOfAirports(self):
    return self.__airport_data
