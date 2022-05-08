from datetime import date
from unittest import defaultTestLoader


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):

			array.append(self.name)
			for childs in self.children:
				childs.depthFirstSearch(array)
			return array
