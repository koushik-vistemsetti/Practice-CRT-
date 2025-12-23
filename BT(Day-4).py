class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
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
            l.append(curr.left)
            if curr.right is None:
                curr.right = new
                return
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

    def postOrderdisplay(self):
        if not self.root:
            return
        st1 = []
        st2 = []
        st1.append(self.root)
        while st1:
            t = st1.pop()
            st2.append(t)
            if t.left:
                st1.append(t.left)
            if t.right:
                st1.append(t.right)
        while st2:
            print(st2.pop().data, end=" ")

    def inOrderdisplay(self):
        c = self.root
        st = []
        while c:
            st.append(c)
            c = c.left
        while st:
            t = st.pop()
            print(t.data, end=" ")
            if t.right:
                c = t.right
                while c:
                    st.append(c)
                    c = c.left

    def levelorder(self):
        s = []
        s.append(self.root)
        while (len(s) != 0):
            l = []
            x = len(s)
            for i in range(x):
                t = s.pop(0)
                l.append(t.data)
                if t.left:
                    s.append(t.left)
                if t.right:
                    s.append(t.right)
            print(l)

    def levelorderReverse(self):
        s = []
        s.append(self.root)
        while (len(s) != 0):
            l = []
            x = len(s)
            for i in range(x):
                t = s.pop(0)
                l.append(t.data)
                if t.right:
                    s.append(t.right)
                if t.left:
                    s.append(t.left)
            print(l)

    def levelOrderSnake(self):
        s = []
        s.append(self.root)
        level = 0
        while (len(s) != 0):
            l = []
            x = len(s)
            for i in range(x):
                t = s.pop(0)
                l.append(t.data)
                if t.left:
                    s.append(t.left)
                if t.right:
                    s.append(t.right)
            if level % 2 == 1:
                print(l[::-1])
            else:
                print(l)
            level += 1

    def onlyLeafs(self):
        s = []
        s.append(self.root)
        leaves = []
        while len(s) != 0:
            t = s.pop(0)
            if not t.left and not t.right:
                leaves.append(t.data)
            if t.left:
                s.append(t.left)
            if t.right:
                s.append(t.right)
        print(leaves)

    def levelorderVertical(self):
        d = {}
        s = [[self.root, 0]]
        while len(s) != 0:
            t = s.pop(0)
            if t[1] in d:
                d[t[1]].append(t[0].data)
            else:
                d[t[1]] = [t[0].data]
            if t[0].left:
                s.append([t[0].left, t[1]-1])
            if t[0].right:
                s.append([t[0].right, t[1]+1])
        for i in sorted(d.keys()):
            print(d[i])

    def topview(self):
        d = {}
        s = [[self.root, 0]]
        while len(s) != 0:
            t = s.pop(0)
            if t[1] not in d:
                d[t[1]] = [t[0].data]
            if t[0].left:
                s.append([t[0].left, t[1]-1])
            if t[0].right:
                s.append([t[0].right, t[1]+1])
        for i in sorted(d.keys()):
            print(d[i])

    def bottomview(self):
        d = {}
        s = [[self.root, 0]]
        while len(s) != 0:
            t = s.pop(0)
            if t[1] not in d:
                d[t[1]] = [t[0].data]
            else:
                d[t[1]].append(t[0].data)
            if t[0].left:
                s.append([t[0].left, t[1]-1])
            if t[0].right:
                s.append([t[0].right, t[1]+1])
        for i in sorted(d.keys(), reverse=False):
            print(d[i][-1], end=" ")
        print()

    def heightoftree(self, node):
        if node is None:
            return 0
        else:
            l = self.heightoftree(node.left)
            r = self.heightoftree(node.right)
            return 1 + max(l, r)

    def diameterTree(self, root):
        global md
        if root is None:
            return 0
        else:
            l = self.heightoftree(root.left)
            r = self.heightoftree(root.right)
            d = 1+l+r
            if md < d:
                md = d
            return 1+max(l, r)

    def sumofDiameter(self, root):
        global ms
        if root is None:
            return 0
        else:
            l = self.sumofDiameter(root.left)
            r = self.sumofDiameter(root.right)
            if ms < l+r+root.data:
                ms = l+r+root.data
            return max(l, r)+root.data

    def check(self, node):
        if node is None:
            return True
        else:
            s = 0
            l = self.check(node.left)
            r = self.check(node.right)
            if node.left:
                s += node.left.data
            if node.right:
                s += node.right.data
            if node.data != s:
                return False
            return l+r+node.data


bt = BinaryTree()
s = []
while input('Do you want to enter: ').lower() != 'n':
    bt.insert(int(input('Enter a Number: ')))

print("Preorder traversal: ")
bt.preOrderdisplay()
print("\nPostorder traversal: ")
bt.postOrderdisplay()
print("\nInorder traversal: ")
bt.inOrderdisplay()
print('\nLevelOrder l->r')
bt.levelorder()
print('\nLevelOrder r->l')
bt.levelorderReverse()
print('\nLevelOrder snake')
bt.levelOrderSnake()
print('\nOnly leafs')
bt.onlyLeafs()
print('\nLevelorder vertical')
bt.levelorderVertical()
print('\nTopview')
bt.topview()
print('\nBottomview')
bt.bottomview()
print('\nHeight of tree')
print(bt.heightoftree(bt.root))
print('\nDiameter of tree')
md = 0
bt.diameterTree(bt.root)
print(md)
ms = 0
print('\nSum of Diameter')
bt.sumofDiameter(bt.root)
print(ms)
print('\nCheck')
print(bt.check(bt.root))
