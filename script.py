print("Hi, The Purpose Of This Software Is To Do A Basic Encoding Algorith, Made By Mohab Gabber\n ")
options = str(input("Do You Want To Encrypt or Decrypt? (E/D): ").lower())
message = str(input("Please Enter Your Message: ").lower())
password = str(input("Enter Your Password: ").lower())
alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
if options == 'e':
	for i in password:
		positions = []
		positions.append(i)
		
elif options == 'd':

else:
	print("That's A Wrong Choice")