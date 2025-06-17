class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left: 'Node' = None
        self.right: 'Node' = None

class BST:
    def __init__(self):
        self.root: 'Node' = None

    def insert(self, value: int):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node: 'Node', value: int):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def sum_tree(self) -> int:
        return self._sum_tree(self.root)

    def _sum_tree(self, node: 'Node') -> int:
        if node is None:
            return 0
        return node.value + self._sum_tree(node.left) + self._sum_tree(node.right)

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

print("The sum of values in the tree is:", bst.sum_tree())