# Menu
# (all menu strings in one place)
class Menu():
  __messagesMain = ""
  __messagesShowInputData = ""
  __messagesCalculatePrice = ""

  def __init__(self):

    # "main" menu
    self.__messagesMain  = "\nSELECT OPTION:\n"
    self.__messagesMain += "1 - show input data\n"
    self.__messagesMain += "2 - calculate price\n"
    self.__messagesMain += "3 - help\n"
    self.__messagesMain += "q - quit\n"

    # "show input data" menu
    self.__messagesShowInputData  = "\nSHOW INPUT DATA (type 1,2,3 or 4)\n"
    self.__messagesShowInputData += "1 - show planes\n2 - show airports list\n3 - show currency rates\n4 - show countries\n"

    # "calculate price" menu
    self.__messagesCalculatePrice = "menu MessagesCalculatePrice"

  def showMainMenu(self):
    choosen = input(self.__messagesMain)
    return choosen;

  def messagesShowInputData(self):
    choosen = input(self.__messagesShowInputData)
    return choosen;

