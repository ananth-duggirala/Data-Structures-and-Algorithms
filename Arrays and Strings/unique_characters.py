"""
Problem statement: Write a program to find out if a string has all unique characters.
"""

def allUniqueCharacters(string):
	lettersPresent = []
	for i in range(len(string)):
		if string[i] in lettersPresent:
			return False
		else:
			lettersPresent += string[i]
	return True

def main():
	string = input("This program will output whether the entered string has all unique characters. \n\nEnter the string: ")
	if allUniqueCharacters(string):
		print("The string has all unique characters.")
	else:
		print("The string does not have all unique characters.")


if __name__ == "__main__":
        main()
