# Binary Search Tree :------------------------------

class BST:
    def __init__(self,key):
        self.key = key
        self.rchild = None
        self.lchild = None
    
#Insert fucntion :--------------------

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else: 
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

# Search Function :------------------

    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the tree")

        else:
            if self.rchild:
                self.rchild.search(data)
            else: print("Node is not present in the tree")

# Pre - order traversal :--------------------

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
        
# In - order traversal :--------------------

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()        
# Post - order traversal :--------------------

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")

#Deletion of node :--------------------
    
    #if root key is empty :---
    def delete(self,data,curr):
        if self.key is None:
            print("Tree is empty")
            return

    #if root key is less than given data :---
        
        if data <self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("Given node is not present in the tree")
   
    #if root key is greater than given data :---
    
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("Given node is not present in the tree")
        else:
            #if contains only one right child :-----
            if self.lchild is None:
                temp =self.rchild
                if data == curr:
                    self.key = temp.key   #whole node copied.
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp =None
                    return
                self = None
                return temp
            #if contains only one left child :-----
            
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp =None
                    return
                self = None
                return temp

            #if contains both childs :-----
            
            node = self.rchild
            while node.lchild:
                node =node.lchild
            self.key = node.key
            self.rchild =self.rchild.delete(node.key,curr)
        return self

# Count Function created outside the class:--------------

def count(node):
    if node is None:
        return 0 
    return 1+count(node.lchild)+count(node.rchild)



root = BST(10)
list1=[1,12]  #4,45,76,67,4,65,99,5
for i in list1:
    root.insert(i)
print("Preorder")
root.preorder()
print()
# print("Inorder Traversal")
# root.inorder()
# print()
print("Total No of Nodes is : ",count(root))
if count(root)>1:
    root.delete(10,root.key)  #root key current hi ho to.
else: 
    print("Cant perform deletion operation")
# print(count(root))
# print("Postorder")
# root.postorder()



