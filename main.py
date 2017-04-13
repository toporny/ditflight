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

		choosen = app.menu.showMainMenu()
		if (choosen == '1'):
			choosen2 = app.menu.messagesShowInputData()
			if (choosen2 == '1'):
				app.showPlanesTable() # #print("1-planes list selected")

			if (choosen2 == '2'):
				app.showAirportTable()  # print("2-airports list selected")

			if (choosen2 == '3'):
				app.showCurrencyArray()  # print("3-currency rates")

			if (choosen2 == '4'):
				app.showCountryCurrencyTable()  # print("4-county currency")
				print("4-country currency")


		if (choosen == '2'):
			print ("2")

		if (choosen == '3'):
			print ("3")
			# app.menu.messagesShowInputData()

		# if (choosen == '2'):
		#   #print ("calculate_price")
		#   app.menu.MessagesCalculatePrice()
		#   #flight_price.calcluatePrice(config)

		if (choosen == 'q'):
		  whLoop = False
		  


main()