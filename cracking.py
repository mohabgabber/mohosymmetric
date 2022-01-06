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
print("Hi, The Purpose Of This Software Is To Do A Basic Cracking Algorith, Made By Mohab Gabber\n ")
print('''
mohosymmetric  Copyright (C) 2022  Mohab Gabber
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
	\n''')
alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '?', '!', '#', '@', '%', '$', '^', '&', '*', '(', ')', '[', ']', '{', '}', '+', '=', '-', '_', '~', '\\', '/', "'", '"', ';', ':', '<', '>', '.', ',']
message = input("Please Enter The Message To Be Cracked: ")
for key in range(len(alphanumeric)):
	plaintext = ''
	for char in message:
		index = alphanumeric.index(char)
		op = (index - key - 2) % len(alphanumeric)
		plaintext += alphanumeric[op]
	print(f"when using the key: {key} the text is: {plaintext}")












