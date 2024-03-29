
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

# recurcive solution for insertting nodes
    # def insertion(self, cur, val):
    #     if not cur:
    #         cur = Node(val)
    #     # elif cur.info == val:
    #     #     return
    #     elif cur.info > val:
    #         cur.left = self.insertion(cur.left, val)
    #     else:
    #         cur.right = self.insertion(cur.right, val)

    #     return cur

    # def insert(self, val):
    #     if not self.root:
    #         self.root = Node(val)
    #     else:
    #         self.insertion(self.root, val)


#    iterative solution for insertting nodes

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return
        root = self.root
        while True:
            if val < root.info:
                if root.left:
                    root = root.left
                else:
                    root.left = Node(val)
                    break
            elif val > root.info:
                if root.right:
                    root = root.right
                else:
                    root.right = Node(val)
                    break


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])
tree.insert(0)
tree.insert(4)
tree.insert(77)
tree.insert(8)

preOrder(tree.root)
