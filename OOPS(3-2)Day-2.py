# Single Linked List
'''
   class node:
       def __init__(self, d):
           self.data = d
           self.next = None


   class SingleLinkedList:
       def __init__(self):
           self.head = None

       def insertFirst(self, x):
           temp = node(x)
           if self.head == None:
               self.head = temp
           else:
               temp.next = self.head
               self.head = temp

       def insertEnd(self, x):
           temp = node(x)
           if self.head == None:
               self.head = temp
           else:
               t = self.head
               while t.next != None:
                   t = t.next
               t.next = temp

       def insertPosition(self, x, p):
           if p == 0:
               self.insertFirst(x)
               return
           temp = node(x)
           t = self.head
           for i in range(p-1):
               t = t.next
               if t.next is None:
                   break
           temp.next = t.next
           t.next = temp

       def deleteFirst(self):
           if self.head == None:
               return
           else:
               self.head = self.head.next

       def deleteEnd(self):
           t = self.head
           if self.head == None:
               return
           elif (t.next == None):
               self.head = None
           elif self.head.next == None:
               self.head = None
           else:
               while t.next.next != None:
                   t = t.next
               t.next = None

       def deletePosi(self, p):
           t = self.head
           if p == 0:
               self.deleteFirst()
               return
           for i in range(p-1):
               t = t.next
               if t.next is None:
                   break
           if t.next is None:
               print('No element at position', p)
               return
           t.next = t.next.next

       def display(self):
           temp = self.head
           while temp:
               print(temp.data, '->', end=" ")
               temp = temp.next
           print('None')

       # Q1
       def detectCycle():
           set = ()
           temp = self.head()
           while temp:
               if id(temp) in s:
                   return True
               s.add(id(temp))
               temp = temp.next
           return False
       # or

       def detectCycles():
           slow = self.head
           fast = self.head
           while fast is not None and fast.next is not None:
               slow = slow.next
               fast = fast.next.next
               if slow == fast:
                   return True
           return False

       def sum(self):
           sum = 0
           temp = self.head
           while temp:
               sum += temp.data
               temp = temp.next
           return sum

       def reverse(self):
           prev = None
           current = self.head
           while current is not None:
               next = current.next
               current.next = prev
               prev = current
               current = next
           self.head = prev
           return

       def search(self, x):
           temp = self.head
           while temp:
               if temp.data == x:
                   return True
               temp = temp.next
           return False

       def sort(self):
           temp = self.head
           l = []
           while temp:
               l.append(temp.data)
               temp = temp.next
           l.sort()
           temp = self.head
           for i in range(len(l)):
               temp.data = l[i]
               temp = temp.next
           return

       def mergeTwoLists(self, l2):
           temp = self.head
           while temp.next is not None:
               temp = temp.next
           temp.next = l2.head
           return



   #'''


# Double Linked List

class node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insertFirst(self, x):
        temp = node(x)
        if self.head is None:
            self.head = temp
            return
        self.head.prev = temp
        temp.next = self.head
        self.head = temp

    def insertLast(self, x):
        temp = node(x)
        if self.head is None:
            self.head = temp
            return
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = temp
            temp.prev = t

    def insertPosition(self, x, p):
        if p == 0:
            self.insertFirst(x)
            return
        temp = node(x)
        t = self.head
        for i in range(p-1):
            t = t.next
            if t.next is None:
                break
        temp.next = t.next
        temp.prev = t
        t.next = temp

    def deleteFirst(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
            return
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

    def deleteLast(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
            return
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.prev.next = None

    def deletePosition(self, p):
        if p == 0:
            self.deleteFirst()
            return
        t = self.head
        for i in range(p-1):
            t = t.next
            if t.next is None:
                break
        t.next = t.next.next
        t.next.prev = t

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, '->', end=" ")
            temp = temp.next
        print('None')

    def sum(self):
        sum = 0
        temp = self.head
        while temp:
            sum += temp.data
            temp = temp.next
        return sum

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            current.prev = next
            prev = current
            current = next
        self.head = prev
        return

    def search(self, x):
        temp = self.head
        while temp:
            if temp.data == x:
                return True
            temp = temp.next
        return False
