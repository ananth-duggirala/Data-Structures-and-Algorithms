"""
Problem statement: Given a string of the form xxxyyzz, return a "compressed string" of the form x3y2z2 if the "compressed string" is shorter 
than the original string, and the original string otherwise.
"""

def find_compressed_string(string):
	compressed_string = ""
	count = 0
	current_letter = string[0]

	for i in range(len(string)):

		if current_letter == string[i]:
			count += 1
		else:
			compressed_string += (current_letter + str(count))
			current_letter = string[i]
			count = 1
		if i == len(string)-1:
			compressed_string += (current_letter + str(count))

	if len(compressed_string) < len(string):
		return compressed_string
	else:
		return string

def main():
	string = input("This program returns a compressed version of the entered string. \n\nEnter string:")
	print("The compressed string is: " + find_compressed_string(string))

if __name__ == "__main__":
	main()
