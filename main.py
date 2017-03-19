# my modules
import dit_flight
   

def main(verbose=True):
  """
  Main loop for application
  """
  app = dit_flight.ditFlight()
  #config = flight_configuration.Configuration()

  
  whLoop = True
  while (whLoop):
    # flight_messages.printAvailableOptions()
    
    choosen = input(app.menu.MessagesMain)
    app.showAirportTable();
  


    # if (choosen == '1'):
    #   app.menu.MessagesShowInputData()
    #   flight_messages.showInputData(config)
      
    # if (choosen == '2'):
    #   #print ("calculate_price")
    #   app.menu.MessagesCalculatePrice()
    #   #flight_price.calcluatePrice(config)
     
    if (choosen == 'x'):
      whLoop = False
      


main()