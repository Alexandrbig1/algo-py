class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: 'Node' = None
        self.right: 'Node' = None


def find_min(node: Node) -> int:
    if node is None:
        return None

    current = node
    while current.left is not None:
        current = current.left

    return current.key


if __name__ == "__main__":
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    print("The minimum value in the tree is:", find_min(root))