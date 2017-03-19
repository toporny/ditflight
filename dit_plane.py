import sys

class Plane():
  def __init__(self, dataArray):
    self.__code = dataArray[0]
    self.__type = dataArray[1]
    self.__units = dataArray[2]
    self.__manufacturer = dataArray[3]
    self.__range = dataArray[4]
    self.__tank = dataArray[5]
    
  
  def getCode(self):
    return self.__code

  
  def getType(self):
    return self.__type

  
  def getUnits(self):
    return self.__units


  def getTankCapacity(self):
    return self.__tank

  
  def getManufacturer(self):
    return self.__units

    
  def getRangeMile(self):
    if (self.__units == 'imperial'):
      return self.__units
    elif (self.__units == 'metric'):
      return self.__units/1.60934      # 1 mile = 1.6093 km
    else:
      print ("Fatal error. Plane unit not specified.")
      sys.exit(-1)


  def getRangeKm(self):
    if (self.__units == 'metric'):
      return self.__units
    elif (self.__units == 'imperial'):
      return self.__units*1.60934      # 1 mile = 1.6093 km
    else:
      print ("Fatal error. Plane unit not specified.")
      sys.exit(-1)






