print("Hi, The Purpose Of This Software Is To Do A Basic Encoding Algorith, Made By Mohab Gabber\n ")
options = str(input("Do You Want To Encrypt or Decrypt? (E/D): ").lower())
message = str(input("Please Enter Your Message: ").lower())
password = str(input("Enter Your Password: ").lower())
def remove(passwords):
    return passwords.replace(" ", "")
alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
if options == 'e':
	positions = []
	actualpositions = []
	finalpositions = []
	for i in remove(password):
		positions.append(i)
	for i in positions:
		actualpositions.append(alphanumeric.index(i))
	for i in actualpositions:
		item = i + 3
		finalpositions.append(item)
	for i in message:
		encrypted = ''
		if i == ' ':
			encrypted += '0'
		else:
			for j in finalpositions:
				indexofitem = alphanumeric.index(i)
				fixedindex = indexofitem + j 
				encrypted += alphanumeric[fixedindex]
	print(encrypted)
#elif options == 'd':
else:
	print("That's A Wrong Choice")