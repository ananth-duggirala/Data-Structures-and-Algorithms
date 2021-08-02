"""
Problem statement: Reverse a string.
"""

def reverseString(string):
	newString = ""
	n = len(string)
	for i in range(n):
		newString += string[n-1-i]
	
	return newString

def main():
	string = input("This program will reverse the entered string. \n\nEnter string: ")
	print(reverseString(string))

if __name__ == "__main__":
	main()
