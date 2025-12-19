'''
#Circular Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class CircularLinkedList:
    def __init__(self):
        self.head=None
    
    def insertFirst(self,ele):
        new=Node(ele)
        if self.head is None:
            self.head=new
            self.head.next=self.head
            self.head.prev=self.head
            print(f'{ele} inserted in the Empty List.\n')
            return
        new.next=self.head
        new.prev=self.head.prev
        self.head.prev=new
        new.prev.next=new
        self.head=new
        print(f'Inserted {ele} at First.\n')

    def insertLast(self,ele):
        new=Node(ele)
        if self.head is None:
            self.insertFirst(ele)
            return
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=new
        new.prev=curr
        new.next=self.head
        self.head.prev=new
        print(f'Inserted {ele} at Last.\n')

    def insertPos(self,ele,pos):
        if pos==1:
            self.insertFirst(ele)
            return
        new=Node(ele)
        curr=self.head
        for i in range(pos-2):
            if curr.next is self.head:
                break
            curr=curr.next
        new.prev=curr
        new.next=curr.next
        curr.next.prev=new
        curr.next=new
        print(f'Inserted {ele} at {pos} position.\n')

    def deleteFirst(self):
        if self.head is None:
            print('List is Empty.\n')
            return
        if self.head.next is self.head:
            print(f'Deleting {self.head.data}.\n')
            self.head=None
            return
        print(f'Deleting {self.head.data} from the First.\n')
        self.head=self.head.next
        self.head.prev=self.head.prev.prev
        self.head.prev.next=self.head

    def deleteLast(self):
        if self.head is None:
            print('List is Empty.\n')
            return
        if self.head.next is self.head:
            print(f'Deleting {self.head.data}.\n')
            self.head=None
            return
        curr=self.head
        while curr.next.next is not self.head:
            curr=curr.next
        print(f'Deleting {curr.next.data} from the Last.\n')
        curr.next=self.head
        self.head.prev=curr

    def deletePos(self,pos):
        if pos==1:
            self.deleteFirst()
            return
        if self.head is None:
            print('List is Empty.\n')
            return
        curr=self.head
        for i in range(pos-1):
            if curr.next is self.head:
                print('Position is Invalid.\n')
                return
            curr=curr.next
        print(f'Deleting {curr.data} from the {pos} position.\n')
        curr.prev.next=curr.next
        curr.next.prev=curr.prev

    def display(self):
        if self.head is None:
            print('Linked List is empty.\n')
            return
        curr=self.head
        while curr.next is not self.head:
            print(curr.data,end='<-->')
            curr=curr.next
        print(curr.data,'None.\n')

    def search(self,ele):
        if self.head is None:
            print('List is Empty')
            return
        curr,c=self.head,1
        while curr.data!=ele:
            if curr.next is self.head:
                print(f'{ele} is Not Found')
                return
            curr,c=curr.next,c+1
        print(f'{ele} is found at position {c}.')
'''

# trees


class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


s = []
while input('Insert Karega?').lower() != 'na':
    t = node(int(input('data likho: ')))
    if len(s) == 0:
        s.append(t)
        s[0].right = None
        s[0].left = None
    else:
        p = (len(s)-1)//2
        if s[p].left != None:
            s[p].left = t
        else:
            s[p].right = t
        s.append(t)


# level order traversal
l = 0
i = 0
while i < len(s):
    c = 2**l
    print([node.data for node in s[i:i+c]])
    i += c
    l += 1
print(l)
