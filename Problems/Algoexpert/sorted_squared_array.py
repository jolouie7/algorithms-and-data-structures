# https://www.algoexpert.io/questions/Sorted%20Squared%20Array

def sortedSquaredArray(array):
	# Soln without sorting
	# 2 pter
	# compare abs val with left and right nums
	# insert from right to left
	squared_lst = []
    left = 0
	right = len(array)-1
	
	while left <= right:
		#place the numbers from right to left
		#if the abs**2 is bigger then place in the front of the squared_lst
			#and move the pter accordingly
		left_num = array[left]
		right_num = array[right]
		if	abs(left_num**2) > abs(right_num**2):
			squared_lst.insert(0, left_num**2)
			left += 1
		else:
			squared_lst.insert(0, right_num**2)
			right -= 1
	return squared_lst