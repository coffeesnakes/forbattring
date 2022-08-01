def threeNumberSum(array, targetSum):
    res = []
    array.sort()
    length = len(array)
    
    for i in range(len(array) - 2):
        j = i + 1
        k = len(array) - 1
        while j < k:
            current = array[i] + array[j] + array[k]
            if current == targetSum:
                res.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
            elif current < targetSum:
                j += 1
            elif current > targetSum:
                k -= 1
            else:
                i += 1
    return res

    #zzzz