def findMedian(arr):
    # Write your code here
    arr.sort()
    half = math.floor(len(arr)/2)
    print('test', half)
    return arr[half]

testArray = [0, 3, 1, 7, 4, 9]

findMedian(testArray)