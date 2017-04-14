import math
import sys


class Price():

	def __init__(self, app):
		# initializes all data
		self.__app = app
		self.__aTravelPoints = []



	def __checkInputData(self, sAairports):
		""" checks input format data """
		""" expected format data is: DUB,GDA,LON """

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

		# test if input data array has duplicated values?
		cleanlist = []
		[cleanlist.append(x) for x in splitted if x not in cleanlist]
		if (len(cleanlist) != len(splitted)):
			print ("Every airport code has to be unique")
			return False


		# test if every airpot exist in datbase
		for code in splitted:
			code_airport_check = False
			if (code in self.__app.airports.getAirportsSymbol()):
				code_airport_check = True
			if (code_airport_check == False):
				print ("I can't find airport code (",code,") in database !!!")
				good_data_format = False

		# if everything is ok store points in self.__aTravelPoints array
		if (good_data_format != False):
			self.__aTravelPoints = splitted

		#return array or false
		return good_data_format



	def __calculateDistance(self, lat1, long1, lat2, long2):

		# Convert latitude and longtitude to radians
		degress_to_radians = math.pi/180.0
		phi = 90 - lat2

		# phi = 90 - latitude
		
		phi1 = (90.0 - lat1)*degress_to_radians
		phi2 = (90.0 - lat2)*degress_to_radians

		# theta = longtitude
		theta1 = long1*degress_to_radians
		theta2 = long2*degress_to_radians

		# Compute spherical distance from spherical coordinates

		cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
		arc = math.acos(cos)

		# Remember to multiply arc by the radius of the earth
		return arc*6371






	def __calculatePrice(self):


		""" calculates the distance and price by sAairports array as a param """
		if (isinstance(self.__aTravelPoints, list) and (len(self.__aTravelPoints)>1)):
			pass # means ok
		else:
			raise ValueError('__calculatePrice() exception error. (self__aTravelPoints) has to be set in this place.')

		dist = self.__calculateDistance(53.421333, -6.270075, 40.639751, -73.778925)
		print (dist)

		#distanceMatrix = 

		# 1km. 1 litr?
		# Density: 840 kg/m³
		# port1: country, city, airport name, airport code, latitude, longitute, price / liter, price/kg, 
		# matrix of distance
		# 			port1,		port2,		port3,		port4,		port5
		# port1		0			12			100			122			65
		# port2		12			0			43			223			76
		# port3		100			43			0			32			87
		# port4		122			223			32			0			99
		# port5		65			76			87			99			0












	def getAirportsAndCalculate(self):

		# debug mode
#		self.__calculatePrice();
#		return 
		#self.__checkInputData('DUB,GDA,ORK')
		self.__aTravelPoints = ['DUB','GDA','WAW','GDA']
		self.__calculatePrice()

		sys.exit(1)
		
		success = False
		while (not success):
			print ("\nType airports separated by comma (max 5) or blank to exit.")
			print ("For example: DUB,GDA,BVA")
			sAairports = input()
			if (self.__checkInputData(sAairports)):
				print ("do calculation...")
				break
			else:
				print ("repeat insert data...")
		return
