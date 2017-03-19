# my modules
import flight_messages
import flight_configuration
import flight_price


    

def main():
  config = flight_configuration.Configuration()
  
  planes = config.getArrayOfPlanes()
  airports = config.getArrayOfAirports()
  # print (airports[1].getAirportName())
  # print (planes[1].getCode())

  
  whLoop = True
  while (whLoop):
    flight_messages.printAvailableOptions()
    choosen = input()
    if (choosen == '1'):
      flight_messages.showInputData(config)
      
    if (choosen == '2'):
      print ("calculate_price")
      #flight_price.calcluatePrice(config)
     
    if (choosen == 'x'):
      whLoop = False
      


main()