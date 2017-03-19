# Menu
# (all menu strings in one place)
class Menu():
  MessagesMain = ""
  MessagesShowInputData = ""
  MessagesCalculatePrice = ""

  def __init__(self):
    self.MessagesMain  = "\nSELECT OPTION:\n"
    self.MessagesMain += "1 - show input data\n"
    self.MessagesMain += "2 - calculate price\nx - exit\n"

    MessagesShowInputData = "\nSHOW INPUT DATA (type 1,2,3 or 4)\n"
    MessagesShowInputData = "1-planes list, 2-airports list, 3-currency rates, 4-countries\n"
    MessagesShowInputData = "\nx - back\n"
    
    MessagesCalculatePrice = "menu MessagesCalculatePrice"
