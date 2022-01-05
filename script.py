print("Hi, The Purpose Of This Software Is To Do A Basic Encoding Algorith, Made By Mohab Gabber\n ")
print('''
mohosymmetric  Copyright (C) 2022  Mohab Gabber
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
	\n''')
def remove(passwords):
    return passwords.replace(" ", "")
alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
options = str(input("Do You Want To Encrypt or Decrypt? (E/D): ").lower())
message = str(input("Please Enter Your Message: ").lower())
password = str(input("Enter Your Password: ").lower())
shifts = int(input("How Many Shifts Do You Want: ").lower())
keychars = []
positions = []
finalpositions = []
key = 0
for i in remove(password):
	keychars.append(i)
for s in keychars:
	positions.append(alphanumeric.index(s))
for e in positions:
	item = e + shifts
	finalpositions.append(item)
for p in finalpositions:
	key += p
if options == 'e':
	encrypted = ''
	for i in message:
		indexed = (alphanumeric.index(i) + key) % len(alphanumeric)
		encrypted += alphanumeric[indexed]
	print(encrypted)
elif options == 'd':
	decrypted = ''
	for i in message:
		indexed = (alphanumeric.index(i) - key) % len(alphanumeric)
		decrypted += alphanumeric[indexed]
	print(decrypted)
else:
	print("That's A Wrong Choice")