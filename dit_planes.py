import prettytable
import sys

class Planes():
  """
  Class Planes - keeps array of every plane
  """
  __planes = []
  
  def __init__(self, arrayOfPlanes):
    """
    makes array of plane objects
    """    
    for row in arrayOfPlanes:
      tmp = Plane(row)
      self.__planes.append(tmp)

    #print(self.__planes)


  def showPlanesTable(self):
    """
    shows all planes inside nice table
    """    
    x = prettytable.PrettyTable(['CODE','TYPE','UNITS','MANUFACTURER','RANGE','TANK_CAPACITY'])
    for plane in self.__planes:
      row = []
      row.append(plane.getCode())
      row.append(plane.getType())
      row.append(plane.getUnits())
      row.append(plane.getManufacturer())
      row.append(plane.getRangeKm())
      row.append(plane.getTankCapacity())
      x.add_row(row)
    print (x)





class Plane():
  """
  Class Plane and all converting methods mile<=>km
  """
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
    """
    Recognizes units and returns mile range for plane
    """
    if (self.__units == 'imperial'):
      return self.__units
    elif (self.__range == 'metric'):
      return int(self.__range)/1.60934      # 1 mile = 1.6093 km
    else:
      print ("Fatal error. Plane unit not specified.")
      sys.exit(-1)


  def getRangeKm(self):
    """
    Recognizes units and returns km range for plane
    """
    if (self.__units == 'metric'):
      return self.__units
    elif (self.__units == 'imperial'):
      return int(self.__range)*1.60934      # 1 mile = 1.6093 km
    else:
      print ("Fatal error. Plane unit not specified.")
      sys.exit(-1)






