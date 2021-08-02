"""
Problem statement: Given two strings, find out if one is a permutation of the other.
"""

def isPermutation(string1, string2):
	string2_list = [letter for letter in string2]
	for i in range(len(string1)):
		isPresent = False
		for j in range(len(string2_list)):
			if string2_list[j] == string1[i]:
				string2_list.pop(j)
				isPresent = True
				break
		if isPresent == False:
			return False
	if string2_list == []:
		return True		

def main():
	print("This program checks whether one string is a permutation of another. \n\n")
	string1 = input("Enter the first string: ")
	string2 = input("Enter the second string: ")

	if isPermutation(string1, string2):
		print("One string is a permuation of another.")
	else:
		print("One string is not a permutation of another.")

if __name__ == "__main__":
	main()
