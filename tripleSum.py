def threeNumberSum(array, targetSum):
	#init trips array to store all sums
	trips = []
	#sort so the three pointers work
	array.sort()
	#loop starts not at the last but 2nd to last because last will be right point start (k)
	for i in range(len(array) - 2):
		#left pointer starts at the smallest value that isn't i, so i+1
		j = i+1
		#right pointer starts at the greatest value
		k = len(array)-1
		#while smaller pointer is less than greatest pointer loop will stop when they meet/cross
		while j < k:
			#variable inside of while loop to store the array of numbers that sum up to targetSum
			currentSum = array[i] + array[j] + array[k]
			#if it's a hit, we append the newfound sum in this instance of the loop to the trips array outside
			if currentSum == targetSum:
				trips.append([array[i], array[j], array[k]])
				#make sure to increment/decrement from current position so loop continues 
				j += 1
				k -= 1
				#if total value less than, increase small pointer
			elif currentSum < targetSum:
				j += 1
				#if total value greater than, decrement largest pointer
			elif currentSum > targetSum:
				k -= 1
	#return trips after appending is done
	return trips
    pass
