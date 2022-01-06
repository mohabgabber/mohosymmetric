'''
mohosymmetric a basic encryption software for testing purposes
Copyright (C) 2022  Mohab Gabber

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import hashlib
print("Hi, The Purpose Of This Software Is To Do A Basic Encoding Algorith, Made By Mohab Gabber\n ")
print('''
mohosymmetric  Copyright (C) 2022  Mohab Gabber
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
	\n''')
option1 = input("Do You Want To Use Caesar Or Vigenere Cipher? (C/V): ").lower()
if option1 == 'c':
	alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '?', '!', '#', '@', '%', '$', '^', '&', '*', '(', ')', '[', ']', '{', '}', '+', '=', '-', '_', '~', '\\', '/', "'", '"', ';', ':', '<', '>', '.', ',']
	option_caesar2 = input("Do You Want To Encrypt or Decrypt? (E/D): ").lower()
	message = input("Please Enter Your Message: ")
	plaintext_password = input("Enter Your Password: ")
	hashed = str(hashlib.sha256(plaintext_password.encode('utf-8')).hexdigest())
	shifts = int(input("How Many Shifts Do You Want: "))
	keychars = []
	positions = []
	finalpositions = []
	key = 0
	for i in hashed:
		keychars.append(i)
	for s in keychars:
		positions.append(alphanumeric.index(s))
	for e in positions:
		item = e + shifts
		finalpositions.append(item)
	for p in finalpositions:
		key += p
	if option_caesar2 == 'e':
		encrypted = ''
		for i in message:
			indexed = (alphanumeric.index(i) + key + 2) % len(alphanumeric)
			encrypted += alphanumeric[indexed]
		print(encrypted)
	elif option_caesar2 == 'd':
		decrypted = ''
		for i in message:
			indexed = (alphanumeric.index(i) - key - 2) % len(alphanumeric)
			decrypted += alphanumeric[indexed]
		print(decrypted)
	else:
		print("That's A Wrong Choice")
elif option1 == 'v':
	pass
	