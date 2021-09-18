'''
Doubly Linked List : each node apart from storing its data has two links. The first link points to the previous node in the list and the 
second link points to the next node in the list.

  #Doubly Linked List :-> Insertion.

'''

# initializing node of a linked list :---------

class Node:     #created node.
    def __init__(self,data):  #node data legi.
        self.data=data  # data liya.
        self.nref=None  # nref = next node refrence start me null hoga.
        self.pref=None #pref = previous node refrence bhi null hoga.
class DoublyLL:  # doubly linked list initialize kri.
    def __init__(self):  
        self.head=None  #start me head null hoga.

# traversal of a node in forward direction:------------

    def printDLL(self):    #same as linked list.
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"<===>",end=" ")
                n=n.nref
            if n is None:
                print("NULL")

# traversal of a node in backward direction:------------

    def printDLL_reverse(self):   #  reverse me krega.
        print()
        if self.head is None:  #agar none h to 
            print("linked list is empty")  #empty print kra dega.
        else:   #varna
            n = self.head  #n ko head banaya.
            while n.nref is not None:  #n ka ref none h ya nhi check krega ye.
                n=n.nref   #n= badhata rhega.
            while n is not None:   #jb tak n none ni h.
                print(n.data,"<===>",end=" ")  #data print kra dega previou node ka or
                n=n.pref   #ye preivous node pr point krta rhega.
            

#inserting in a empty node:---------

    def insert_empty(self,data):  
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

#inserting at begin of a node:---------

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

#inserting at end of a node:---------

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

#inserting after of a given node:---------


    def add_after(self,data,x):
        if self.head is None:
            print("LL is empty!")
        else:
            n =self.head
            while n is not None:
                if x==n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
                
#inserting before of a given node:---------

    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x==n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref                
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node



DLL=DoublyLL()
DLL.add_begin(5)
DLL.add_begin(7)
DLL.add_after(8,5)
# DLL.insert_empty(4)
DLL.printDLL()
DLL.printDLL_reverse()



































