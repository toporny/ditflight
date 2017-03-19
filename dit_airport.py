class Airport():
  
  def __init__(self, dataArray):
    self.__airportId          = dataArray[0]
    self.__airportName        = dataArray[1]
    self.__airportCity        = dataArray[2]
    self.__airportCountry     = dataArray[3]
    self.__airportCode        = dataArray[4]
    self.__airportCode2       = dataArray[5]
    self.__airportLatitude    = dataArray[6]
    self.__airporttLongtitude = dataArray[7]
    self.__airportIdontKnow1  = dataArray[8]
    self.__airportIdontKnow2  = dataArray[9]
    self.__airportIdontKnow3  = dataArray[10]
    self.__airportTimezone    = dataArray[11]



  def getAirportId(self):
    return self.__airportId
    
  def getAirportName(self):
    return self.__airportName
    
  def getAirportCity(self):
    return self.__airportCity
    
  def getAirportCountry(self):
    return self.__airportCountry
    
  def getAirportCode(self):
    return self.__airportCode
    
  def getAirportLatitude(self):
    return self.__airportLatitude
    
  def getAirporttLongtitude(self):
    return self.__airporttLongtitude
    
    
