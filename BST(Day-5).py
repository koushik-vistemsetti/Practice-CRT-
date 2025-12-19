class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def insertBST(root, x):
    t = Node(x)
    if root is None:
        return t
    p = None
    q = root
    while q is not None:
        p = q
        if t.data < q.data:
            q = q.left
        elif t.data > q.data:
            q = q.right
        else:
            return root
    if t.data < p.data:
        p.left = t
    else:
        p.right = t
    return root


def insertRecr(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insertRecr(root.left, x)
    elif x > root.data:
        root.right = insertRecr(root.right, x)
    return root


def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


def inOrderSuccessor(root):
    q = root
    while q.left is not None:
        q = q.left
    return q


def inOrderSuccessorR(root):
    q = root
    while q.right is not None:
        q = q.right
    return q


def deleteNode(root, data):
    if not root:
        return root
    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif data > root.data:
        root.right = deleteNode(root.right, data)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        # for inorder successor

        temp = inOrderSuccessor(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
        '''
        temp = inOrderSuccessorR(root.left)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
        '''
    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)


root = None
keys_to_insert = [50, 30, 20, 40, 70, 60, 80]
for key in keys_to_insert:
    root = insertBST(root, key)

print("InOrder traversal of original BST:")
inorder_traversal(root)
print("\n")

x = 40
result = search(root, x)
if result:
    print(f"Key {x} found in the BST")
else:
    print(f"Key {x} not found in the BST")

root = deleteNode(root, 70)
print("\nInorder traversal after deleting node 70:")
inorder_traversal(root)
print("\n")

root = deleteNode(root, 20)
print("\nInorder traversal after deleting node 20:")
inorder_traversal(root)
print("\n")
