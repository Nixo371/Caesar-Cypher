def shift_letter(letter, shift):
	lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	i = 0
	for element in lowercase:	# Runs through each letter in the above arrays, until it finds one
		if element == letter:	# Shifts it forwards by the specified shift value then returns it
			if i + shift > 25:
				return(lowercase[i + shift - 26]) 	# If the specified shift makes it go past the 25th index (z)
			else:									# subtract 26 so as to 'loop' back to the beginning (a)
				return(lowercase[i + shift])
		i += 1
	i = 0
	for element in uppercase:
		if element == letter:
			if i + shift > 25:
				return(uppercase[i + shift - 26])
			else:
				return(uppercase[i + shift])
		i += 1
	return(letter) # If the letter is not found (in case of number/symbol), return the character that was passed

def decryption(string):
	shift = 1
	file.write("Decryption of the string '" + string + "'\n\n") # "Title" of the file
	while shift < 27:									# Writes each letter to the file and appends with line skip
		for element in string:							# Writes every possible combination, separated by line skips
			file.write(shift_letter(element, shift))
		file.write("\n")
		shift += 1

def encryption(string):
	shift = 0
	while shift < 1 or shift > 25:
		shift = int(input("Enter the amount to shift by (1-25): ")) # Asks the user how much to shift by until they give a valid answer
		if shift < 1 or shift > 25:
			print("That is not a number between 1 and 25")
	file.write("Encryption of the strin '" + string + "' with a shift of " + str(shift) + "\n\n")
	for element in string:
		file.write(shift_letter(element, shift))	# Writes the output to the file
	file.write("\n")

# Main function, asks the user for decryption/encryption then executes the corresponding function

file = open("caesar_output.txt", "w") # Sets the file 'caesar_output.txt' to be overwritten, or creates if it doesn't exist
selection = input("Would you like to (D)ecrypt or (E)ncrypt?")
if selection == 'D' or selection == 'd':
	decrypt = input("Enter the string to decrypt: ")
	decryption(decrypt)
elif selection == 'E' or selection == 'e':
	encrypt = input("Enter the string to encrypt: ")
	encryption(encrypt)
else :
	print("Sorry, that's not a valid option")
