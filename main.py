# my modules
import flight_messages
import dit_data
import prettytable

class Menu():
  
  def MessagesMain(self):
    print ("menu MessagesMain")
    return
  
  def MessagesShowInputData(self):
    print ("menu MessagesShowInputData")
    return

  def MessagesCalculatePrice(self):
    print ("menu MessagesCalculatePrice")
    return



class ditFlight():
  
  def __init__(self):
    __data = dit_data.ditData()
    self.planes = __data.getArrayOfPlanes()
    self.airports = __data.getArrayOfAirports()
    #__menu = Menu()
    self.menu = Menu()


  def showPlanesTable(self):
    x = prettytable.PrettyTable(['code','type','units','manufacturer','range','tank_capacity'])
    for row in self.planes:
      x.add_row(row)
    print (x)    


  def showAirportTable(self):
    # 668,Lech Walesa,Gdansk,Poland,GDN,EPGD,54.377569,18.466222,489,1,E,Europe/Warsaw
    x = prettytable.PrettyTable(["ID","NAME","CITY","COUNTRY","CODE"])
    for row in self.airports:
      x.add_row([row[0], row[1][:20], row[2][:15], row[3][:13], row[4][:5]])
    print (x)    


  def calculateDistance(airport1, airport2):
    return 44

    

def main():

  app = ditFlight()
  #config = flight_configuration.Configuration()

  
  whLoop = True
  while (whLoop):
    # flight_messages.printAvailableOptions()
    app.menu.MessagesMain()
    choosen = input()
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