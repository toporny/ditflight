def printAvailableOptions():
  print ("\nSELECT OPTION:")
  print ("1 - show input data")
  print ("2 - calculate price")
  print ("x - exit")

def showInputData(config):

  ehLoop = True
  while (ehLoop):
    print ("\nSHOW INPUT DATA (type 1,2,3 or 4)")
    print ("1-planes list, 2-airports list, 3-currency rates, 4-countries")
    print ("x - back")
    choosen2 = input()
    
    if (choosen2 == '1'):
      config.showPlanesTable()

    if (choosen2 == '2'):
      config.showAirportsTable()
      print ("if you want to see more details about airport please type: 2,airport_code")
      print ("For example: 2,DUB")
      
    if (len(choosen2) == 5):
      print ("airport details!!!!!!!!!!!!!!!!!!!!!!!!!")
      
      
      
    if (choosen2 == 'x'):
      ehLoop = False
