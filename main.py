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

		# menu structure
		# ------------------------------
		# 1 - show input data
		#		1 - show planes
		#		2 - show airports list
		#		3 - show currency rates
		#		4 - show countries		
		# 2 - calculate price
		# 3 - help
		# q - quit
		menu_choosen = app.menu.showMainMenu()

		if (menu_choosen == '1'):
			submenu_choosen = app.menu.showSubMenu()

		if (menu_choosen == '2'):
			app.price.getAirportsAndCalculate()


		if (menu_choosen == '3'):
			print ("3")

		if (menu_choosen == 'w'):
			app.showCountryCurrencyTable()
			# app.menu.messagesShowInputData()

		# if (menu_choosen == '2'):
		#   #print ("calculate_price")
		#   app.menu.MessagesCalculatePrice()
		#   #flight_price.calcluatePrice(config)

		if (menu_choosen == 'q'):
			whLoop = False

		pass
		  


main()