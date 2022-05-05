def cleanMiniMaxSum(arr):
    arr.sort()
    # Write your code here
    minSum, maxSum = 0, 0
    for i in range(len(arr) - 1):
        minSum = minSum + arr[i]
    for j in range(1, len(arr)):
        maxSum = maxSum + arr[j]
    print(str(minSum) + ' ' + str(maxSum))



def miniMaxSum(arr):
    arr.sort()
    print(arr)
    # Write your code here
    minSum, maxSum = 0, 0
    for i in range(len(arr) - 1):
        minSum = minSum + arr[i]
    for j in range(1, len(arr)):
        print(maxSum)
        maxSum = maxSum + arr[j]
        print('a: ',maxSum)
    print(str(minSum) + ' ' + str(maxSum))


xray = [7, 69, 2, 221, 8974]
print(xray)
test = xray.sort()
print(test)
nray = [1, 2, 3, 4, 5]
miniMaxSum(xray)
#ar = [-4, 3, -9, 0, 4, 1]
