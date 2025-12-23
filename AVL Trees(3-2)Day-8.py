class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        new = Node(x)
        if self.root is None:
            self.root = new
            return
        l = [self.root]
        while l:
            curr = l.pop(0)
            if curr.left is None:
                curr.left = new
                return
            if curr.left != 'n':
                l.append(curr.left)
            if curr.right is None:
                curr.right = new
                return
            if curr.right != 'n':
                l.append(curr.right)

    def preOrderdisplay(self):
        if not self.root:
            return
        st = []

        st.append(self.root)
        while st:
            t = st.pop()
            print(t.data, end=" ")
            if t.right:
                st.append(t.right)
            if t.left:
                st.append(t.left)

    def BalanceFactor(self, node):
        if node is None:
            return 0
        if abs(self.height(node.left) - self.height(node.right)) > 1:
            return -1
        if node.left is not None:
            self.BalanceFactor(node.left)
        if node.right is not None:
            self.BalanceFactor(node.right)
        return 0

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    # def printfromRightmos


bt = AVLTree()
while input('Do you want to enter (y/n): ').lower() != 'n':
    bt.insert((input('Enter a Number: ')))

if (bt.BalanceFactor(bt.root) == -1):
    print("Balanced")
else:
    print("Not Balanced")

bt.preOrderdisplay()
