class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None


def branchSums(root):
	sums = []
    calcSums(root, 0, sums)
	return sums

def calcSums(node, branchSum, sums):
	if node is None:
		return
	#adds up sum of each node as we progress through the branch
	branchSum = branchSum + node.value
	#check if we're at a leaf, thus have the branch's sum and adds the value to sums array
	if node.left is None and node.right is None:
		sums.append(branchSum)
		return
	#Recursively run calcSums within itself
	calcSums(node.left, branchSum, sums)
	calcSums(node.right, branchSum, sums)
