class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: 'Node' = None
        self.right: 'Node' = None


def find_max(node: Node) -> int:
    if node is None:
        return None

    current = node
    while current.right is not None:
        current = current.right

    return current.key


if __name__ == "__main__":
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.right.right = Node(80)
    root.right.left = Node(60)

    print("The maximum value in the tree is:", find_max(root))