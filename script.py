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
import string
print("Hi, The Purpose Of This Software Is To Do A Basic Encoding Algorith, Made By Mohab Gabber\n ")
print('''
mohosymmetric  Copyright (C) 2022  Mohab Gabber
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
	\n''')
option1 = input("Do You Want To Use Caesar Or Vigenere Cipher? (C/V): ").lower()
option2 = input("Do You Want To Encrypt or Decrypt? (E/D): ").lower()
ascii_chars = string.printable
message = input("Please Enter Your Message: ")
plaintext_password = input("Enter Your Password: ")
key = str(hashlib.sha256(plaintext_password.encode('utf-8')).hexdigest())
encrypted = ''
decrypted = ''
key_index = 0
if option1 == 'c':
	keychars = []
	positions = []
	finalpositions = []
	keys = 0
	for i in key:
		keychars.append(i)
	for s in keychars:
		positions.append(ascii_chars.index(s))
	if option2 == 'e':
		encrypted = ''
		for i in message:
			indexed = (ascii_chars.index(i) + keys + 2) % len(ascii_chars)
			encrypted += ascii_chars[indexed]
		print(encrypted)
	elif option2 == 'd':
		decrypted = ''
		for i in message:
			indexed = (ascii_chars.index(i) - keys - 2) % len(ascii_chars)
			decrypted += ascii_chars[indexed]
		print(decrypted)
	else:
		print("That's A Wrong Choice")
elif option1 == 'v':
	if option2 == 'e':
		for char in message:
			index = (ascii_chars.index(char) + (ascii_chars.index(key[key_index]))) % len(ascii_chars)
			encrypted += ascii_chars[index]
			key_index += 1
			if key_index == len(key):
				key_index = 0
		print(encrypted)
	elif option2 == 'd':
		for char in message:
			index = (ascii_chars.index(char) - (ascii_chars.index(key[key_index]))) % len(ascii_chars)
			decrypted += ascii_chars[index]
			key_index += 1
			if key_index == len(key):
				key_index = 0
		print(decrypted)
	