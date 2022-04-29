
def findClosestValueInBst(tree, target):
    # Write your code here.
	return bstHelp(tree, target, tree.value)
    pass

def bstHelp(tree, target, currentClosest):
	node = tree
	while node is not None:
		if abs(target - node.value) < abs(target - currentClosest):
			currentClosest = node.value
		if node.value > target:
			node = node.left
		elif node.value < target:
			node = node.right
		else:
			break
	return currentClosest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
