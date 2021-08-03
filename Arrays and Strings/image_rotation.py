"""
Problem statement: Rotate an image, represented as a 2D array, by 90 degrees, clockwise
"""

def rotate_image(image_array, N): # image_array is an N*N 2D array
	new_array = [[0 for i in range(N)] for j in range(N)]
	for i in range(N):
		for j in range(N):
			new_array[j][N-1-i] = image_array[i][j]

	return new_array

def print_matrix(arr, N):
	for i in range(N):
		for j in range(N):
			print(arr[i][j], end=" ")
		print("")

def main():
	N = int(input("Enter N: "))
	image_array = []

	print("Enter an array in the following format: \n1 2 3\n4 5 6 \n7 8 9\n")
	for i in range(N):
		image_array.append([j for j in input().split()])

	print("")
	print_matrix(rotate_image(image_array, N), N)

if __name__ == "__main__":
	main()
