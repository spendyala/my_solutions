class Node(object):
    def __init__(self, data, child=None):
        self.data = data
        self.child = None
        if not self.child:
            self.child = []
        if type(child) == list:
            self.child = child

    def add_child(self, child):
        self.child.append(child)


def least_common_ancestor(root, node_1, node_2):
    if not root:
        return None
    if root.data == node_1.data or root.data == node_2.data:
        return root
    count = 0
    temp = None
    for each_child in root.child:
        val = least_common_ancestor(each_child, node_1, node_2)
        if val:
            temp = val
            count += 1
        if count >= 2:
            return root
    return temp

a = Node('a')

b = Node('b')
c = Node('c')
d = Node('d')

e = Node('e')
f = Node('f')
g = Node('g')

h = Node('h')
i = Node('i')
j = Node('j')

a.add_child(b)
a.add_child(c)
a.add_child(d)

b.add_child(e)
b.add_child(f)
b.add_child(g)

c.add_child(h)
c.add_child(i)
c.add_child(j)

assert least_common_ancestor(a, Node('b'), Node('c')) == a
assert least_common_ancestor(a, Node('e'), Node('h')) == a
assert least_common_ancestor(a, Node('i'), Node('j')) == c
assert least_common_ancestor(a, Node('d'), Node('e')) == a
assert least_common_ancestor(a, Node('d'), Node('j')) == a
