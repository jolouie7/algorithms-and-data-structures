# https://www.algoexpert.io/questions/Two%20Number%20Sum

def twoNumberSum(array, targetSum):
	# store the compliment in a lst
	# if target - currNum in the compliment lst then return both nums in an list
	# Once we have gone through the entire array, return []
	
	compliment_lst = []
	for num in array:
		if num in compliment_lst:
			return [num, targetSum-num]
		else:
			compliment_lst.append(targetSum - num)
	
	return []