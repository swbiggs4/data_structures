# in order 
# go(left)
# me
# go(right)
# post order
# go(left)
# go(right)
# me
# pre order p
# me 
# go(left)
# go(right)
#   O(logN) for balanced trees, O(N) worst case


class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val
    def find(self, data):
        if self.data==data:
            return True
        elif data < self.data:
            return self.l_child.find(data)
        elif data > self.data:
            return self.r_child.find(data)
        return False

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if node.data < root.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    # go(left)
    # me 
    # go(right)
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def pre_order_print(root):
    # me 
    # go(left)
    # go(right)
    if not root:
        return        
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)   