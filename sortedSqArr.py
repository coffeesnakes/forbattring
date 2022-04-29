def sortedSquaredArray(array):
	sqArr = []
    for i in array:
		push = i*i
		sqArr.insert(len(array), push)
	print(sqArr)
	sqArr.sort()
	return sqArr
    return []
