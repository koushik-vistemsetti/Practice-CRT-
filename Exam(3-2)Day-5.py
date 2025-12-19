# Question 1
'''
import math as m
class node:
    def __init__(self, d):
        self.data=d
        self.next=None


class SingleLinkedList:
    def __init__(self):
        self.head=None

    def insertFirst(self, x):
        temp = node(x)
        if self.head==None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp

    def insertEnd(self, x):
        temp=node(x)
        if self.head==None:
            self.head=temp
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next=temp

    def display(self):
        temp=self.head
        while temp:
            print(temp.data, '->', end=" ")
            temp=temp.next
        print('None')

    def rotate(self,k):
        i=1
        while i<=k:
            if not self.head or not self.head.next:
                return self.head
            prev=None
            t=self.head
            while t.next:
                prev=t
                t=t.next
            prev.next=None
            t.next=self.head
            self.head=t
            i+=1
        

ll=SingleLinkedList()
while input('do u want to Enter a Number') != 'n':
    c=0
    n=int(input('Enter a Number'))
    for i in range(2,m.isqrt(n)+1):
        if(n%i==0 ):
            if(n//i==i):
                c+=1
            else:
                c+=2
    if(c>0):
        ll.insertEnd(n)
    else:
        ll.insertFirst(n)
    ll.display()

 #  Question 2 Rotate A list
    
ll=SingleLinkedList()
li=[1,2,3,4,5,6]
for i in range(len(li)):
    ll.insertEnd(li[i])
k=int(input('How many times you want to rotate:'))
ll.rotate(k)
ll.display()

'''
# Ouestion 3 BT and display INORDER


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

    def inOrderdisplay(self):
        c = self.root
        st = []
        st.append(c)


bt = BinaryTree()
s = []
while input('Do you want to enter: ').lower() != 'n':
    bt.insert(int(input('Enter a Number: ')))
bt.preOrderdisplay()
