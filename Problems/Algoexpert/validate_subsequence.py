# https://www.algoexpert.io/questions/Validate%20Subsequence

def isValidSubsequence(array, sequence):
	# use 2 pters
	# start at idx 0 for both lists, move left array pter each time
	# move both pters when we find a match
	# we return true when idx of sequence is == len(sequence)
	# return false if idx of array == len(array) and idx of sequence != len(sequence)
	
	seq_pter = 0
	
	for num in array:
		if seq_pter == len(sequence):
			return True
		elif num == sequence[seq_pter]:
			seq_pter += 1
			
	if seq_pter != len(sequence):
		return False
	else:
		return True