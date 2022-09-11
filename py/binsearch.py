
# BINARY SEARCH
# Alicia Wade
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: GeeksforGeeks and Java Program from Summer

# Returns index of x in arr if present, else -1
def bin_Search(arr, lowPos, highPos, target):

	# Check base case
	if highPos >= lowPos:

		mid = (highPos + lowPos) // 2

		# If element is present at the middle itself
		if arr[mid] == target:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > target:
			return bin_Search(arr, lowPos, mid - 1, target)

		# Else the element can only be present in right subarray
		else:
			return bin_Search(arr, mid + 1, highPos, target)

	else:
		# Element is not present in the array
		return -1

# Test array
arr = [ 22, 3, 4, 10, 40,45,23 ]
target = 3

# Function call
result = bin_Search(arr, 0, len(arr)-1, target)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")

