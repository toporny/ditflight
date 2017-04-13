class Price():

	def __init__(self, app):
		# initializes all data
		self.__app = app
		self.__aTravelPoints = []



	def __checkInputData(self, sAairports):
		good_data_format = True
		self.__aTravelPoints = []

		# make upper case for whole string
		sAairports = sAairports.upper();
		
		# remove spaces from whole string "DUB, GDA , WAW" => "DUB,GDA,WAW"
		sAairports = sAairports.replace(" ", "")

		# split to array with 3chars code
		splitted = sAairports.split(',')

		# test if it is at least two airports and max 5
		if ((len(splitted) <= 1) or (len(splitted) > 5)):
			print ("please type minimum two airports codename and maximum 5 !!!")
			good_data_format = False

		# test if every code has exactly three chars
		for x in splitted:
			if (len(x) != 3):
				print ("Wrong airport code (",x,").Every airport code should have exactly 3 chars !!!")
				good_data_format = False

		# test if every airpot exist in datbase
		for code in splitted:
			code_airport_check = False
			for airport in self.__app.airportsArray:
				if (airport[4] == code):
					code_airport_check = True
			if (code_airport_check == False):
				print ("I can't find airport code (",code,") in database !!!")
				good_data_format = False				

		self.__aTravelPoints = splitted
		return good_data_format



	def __calculatePrice(self):
		""" calculates the distance and price by sAairports array as a param """
		if (isinstance(sAairports, list) and (len(sAairports)>1)):
			pass # means ok
		else:
			raise ValueError('__calculatePrice() exception error. (self__aTravelPoints) has to be set in this place.')

		# 1km. 1 litr?
		# Density: 840 kg/m³
		# port1: country, city, airport name, airport code, latitude, longitute, price / liter, price/kg, 
		# matrix of distance
		# 		port1,		port2,		port3,		port4,		port5
		# port1		x			12									
		# port2		12			x									
		# port3								x						
		# port4											x			
		# port5														x









	def getAirportsAndCalculate(self):

		# debug mode
		self.__calculatePrice();
		return 

		success = False
		while (not success):
			print ("\nType airports separated by comma (max 5) or blank to exit.")
			print ("For example: DUB,GDA,BVA")
			sAairports = input()
			if (sAairports == 'test'):
				sAairports = 'dub,gda,waw'
				print (sAairports )
			if (self.__checkInputData(sAairports)):
				print ("do calculation...")
				break
			else:
				print ("repeat insert data...")
		return
