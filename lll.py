# Given a list, write a Python program to swap first and last element of the list.


# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]
test1 = [12, 35, 9, 56, 24]
test2 = [1, 2, 3]


def firstLastSwap (list):

    size = len(list)
  
    last = list[size - 1]
    first = list[0]
  
    swapped = list.copy()
    swapped[0] = last
    swapped[size - 1] = first
  
    return swapped
print(test1)
print(firstLastSwap(test1))
print(test2)
print(firstLastSwap(test2))