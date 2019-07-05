#
#Password Generator
#Created by Barnabas Obeng-Gyasi
#Created July 3, 2019
#Last Updated July 3, 2019

import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890!?.-'

length = int(input('How many characters do you want in your password?'))
number_of_passwords = int(input('How many passwords do you want generated?'))
for p in range (number_of_passwords):
	password = ''
	for c  in range(length):
		password += random.choice(chars)
	print(password)
