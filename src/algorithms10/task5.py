import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque


class Node:
    def __init__(self, key, color="#03a9f4"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def heap_to_tree(heap, index=0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    node.left = heap_to_tree(heap, left_index)
    node.right = heap_to_tree(heap, right_index)
    return node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def generate_colors(n):
    return [f'#{int(255 * (i / (n - 1))):02X}96F0' for i in range(n)]


def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def bfs_visualize(root):
    queue = deque([root])
    total_nodes = count_nodes(root)
    colors = generate_colors(total_nodes)

    i = 0
    while queue:
        node = queue.popleft()
        node.color = colors[i]
        i += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        draw_tree(root)


def dfs_visualize(root):
    stack = [root]
    total_nodes = count_nodes(root)
    colors = generate_colors(total_nodes)

    i = 0
    while stack:
        node = stack.pop()
        node.color = colors[i]
        i += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        draw_tree(root)


heap = [3, 5, 9, 6, 8, 20, 10]
heapq.heapify(heap)
root = heap_to_tree(heap)

print("BFS traversal:")
bfs_visualize(root)

print("DFS traversal:")
dfs_visualize(root)