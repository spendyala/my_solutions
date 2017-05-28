class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def least_common_ancestor(root, node_1, node_2):
    if not root:
        return None
    if root.data == node_1.data or root.data == node_2.data:
        return root
    left_return_node = least_common_ancestor(root.left, node_1, node_2)
    right_return_node = least_common_ancestor(root.right, node_1, node_2)
    if left_return_node and right_return_node:
        return root
    return left_return_node if left_return_node else right_return_node

node_m = Node('m')
node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_p = Node('p')
node_q = Node('q')
node_r = Node('r')

node_m.left = node_a
node_m.right = node_p

node_a.left = node_b
node_a.right = node_c

node_p.left = node_q
node_p.right = node_r

node = least_common_ancestor(node_m, Node('c'), Node('p'))
assert node.data == 'm'
node = least_common_ancestor(node_m, Node('b'), Node('a'))
assert node.data == 'a'
