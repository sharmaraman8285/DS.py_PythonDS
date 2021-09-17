''' 
Linked list :  a linked list consists of nodes where each node contains a data field and a reference(link) to the next node in the list.

     Types: #  Singly Linked List.
            #  Doubly Linked List.
            #  Circular Linked List.


#Singly Linked List : Deletion

'''


# Node initialization:-----------------------

class Node:  #node banayenge
     def __init__(self,data):  #node me phele data dekhenge.
         self.data = data   #agar head me data hai ya nhi.
         self.ref = None  #refrence null hoga start me khali ka.

#linked List intialization:--------------------
class LinkedList:   #linked list banayi.
     def __init__(self):  #initialize kri.
          self.head =None  #shuru me head khali hoga.

#traversal the node and print the element:---------------------
     def printLL(self):           
          if self.head is None:                           #agar head null hai.
               print("Liknked list Empty hai ")                #empty print kra dega.
          else:                                          #varna fir..
               n=self.head                            #n me head lega.
               while n is not None:                 #agar n null nhi h.
                    print(n.data,"--->",end=" ")   #print kra dega
                    n= n.ref      
                    if n is None:
                         print("Null")        #or fir  n ko ref wale address pr bhejega data print krane fir loop me jayega data dekhega null hoga to null varna print kra dega.

# add at the beggining of the node:------------------

     def add_begin(self,data):    #data lega or ek new node banayega.
          new_Node = Node(data)   #node function me jakar data lega or new node ban jayegi jiska ref none hoga node class ke hisaab se.
          new_Node.ref = self.head  # ab new node ka refrence hoga dusre ka head.
          self.head=new_Node   #or head ab new node khud pr point kregi.

# add at the ending of the node:------------------

     def add_end(self,data):   #data lega node banayega.
          new_Node=Node(data)    #node class se init. krega data lekar node ban jayegi.
          if self.head is None:   #check krega agar head hi null h to.
               self.head = new_Node   #head to new node pr point kr dega.
          else:           #varna
              n=self.head    #n ko head ke data pr point krega.
              while n.ref is not None:  #or dekega ki n ka data null hua ya nhi
                   n=n.ref   # n ko n ke refrence pr badhata jayega or loop chalta jayega agar null ni h to.
              n.ref =new_Node   #jb null ho jayega to last ke refrence ko apne head pr point kra dega or end me add ho jayga.


# add after the node:------------------

     def add_after_node(self,data,x):  # data ke sath ek value lenge jiske baad value insert krni h.
          n=self.head     # n ko head bana denge.
          while n is not None:    #jab n none nhi h to.
               if x==n.data:      # jb tak n ke data ki value x ke barabar na ho jaye.
                    break  #babar ho jaye to break krde loop bhar aa jaye.
               n=n.ref   # n update hokar x ke baad ki value ka refrence me jayega.
               if n is None:  # agar last node bhi null hai to kh dega present ni h.
                    print("Node is not present in the LL")  # 
               else:  #varna
                    new_Node=Node(data)    #new node create krenge data lenge usme.
                    new_Node.ref =n.ref   #jo purani node ka refrence tha ab new node ke refrence pr point kr dega.
                    n.ref = new_Node     # jo phele n tha before node me ab uska refrence new node ke head ko bana denge.

# add before the node:------------------

     def add_before_node(self,data,x):    #before me bhi same data or x lega jis se phele insert krna h.
        if self.head is None:    # agar insert krne se phele hi head none h.
            print("Linked List is empty!")    #print kra do link list khali h.
            return    #or vapis aa jayo.
        if self.head.data==x:    #agar head ka data x ke barbar h. matlv pheli hi node pr mil gya vo jis se phele node insert krani h.
            new_node = Node(data)   # to ye add_bfore node ka concept laga do.
            new_node.ref = self.head   #new_node ka refrence dusre ke head ko point krega.
            self.head = new_node  #or head ko khud pr point kra lega.
            return  #return kr dega jo bhi aya vha.
        n = self.head     #agar nhi hua pehli node pr vo element to n ko head pr point kra dega.
        while n.ref is not None:    #jab tak n ka refrence null nhi h to matlv usme next element pr jayega refrence se.
            if n.ref.data==x:   # while me ghus kr n ke refrence ka data x ke barabar h ya nhi check krega.
                break    #agar n ka data ka refrence x ke barabr h to vahi break krke loop se bhar ayega.
            n = n.ref        #loop se bhar akar n ko refrence pr point krayega.
        if n.ref is None:   # agar uska refrence null h to.
            print("Node is not found!")  #matlav end pr aa gya or node ni mila jiske phele insert krna hai.
        else:  #varna
            new_node = Node(data)  #new node create krega.
            new_node.ref = n.ref  #new node ka refrence agle node pr point krega.
            n.ref = new_node    #or phele node ka refrence apne head pr kra lega.

# Node Deletion Start from here:------------------------------------

   #delete form begin.....----------------------

     def delete_begin(self):  #isme data nhi lenge kyuki delete hi krna h bas:
        if self.head is None:    #agar head hi none hoga to.
            print("no nodes in the linked list ")  # print kra do node me element hi nhi hai.
        else:  #varna fir agar none nhi h to.
            self.head=self.head.ref   # phele wale ke head ko phele wale ke refrence pr point kra denge or vo head ban jayega.

#Delete form end.....----------------------
     def delete_end(self):   #end me se element delete krne ke liye.
          if self.head is None:   #agar head hi none h to.
               print("node not prenset in the link list")  #node hi nhi h.
          elif self.head.ref is None:  #varna agar ek hi element to uska ref. nhi hoga fir to koi
               self.head=None  #usi element ke head ko none/null pr point kra dega to head ho null ho jayega
          else:  #varna agar no. of element h usme kuch.
               n=self.head  #to n ko head banayega.
               while n.ref.ref is not None:  #n ke ref ke ref ko dekhege ki null to nhi h, is se 2nd last node pr phuch jayenge loop me.
                    n=n.ref  #n ki value change hoti rhegi 2nd last tak phuchne ke liye.
               n.ref = None  #phuch kr 2nd last ke ref ko none kr dega jis se last wala element delete ho jayega.
  
#Delete form middle/ by value :-------------------------
     def delete_by_value(self,x):  #delete ke liye value lenge jise delete krna hai.
          if self.head is None:  #agar head hi none h 
               print("cant delete linked list is empty")  #delete ni kr skte empty ko.

          if x==self.head.data:  #agar x ki or head ke data ki value same h to.
               self.head =self.head.ref    #head ko head ke refrence wale pr point kr deneg or vo head ban jayega.
               return   #else bhi laga skte h.
          n=self.head   #n ko head bana denge.
          while n.ref is not None:  #jab tak n ka ref none nhi ho jata
               if x==n.ref.data:    #or x n ke refrene pr jo data h uske barabar ni hota. or jese hi barabar hoga.
                    break  #break kr dega loop se  bhar aa jayega.
               n=n.ref   #n ko ref pr badhata jayega loop ka part h.
               if n.ref is None:  #fir dekhega n ka ref none h kya.
                    print("node is not present")  #agar none h to poori node traverse krdi usay ni mila node.
               else:  # agar mil jayega node
                    n.ref=n.ref.ref  #to uska ref ko n ke ref ke ref ko point kr dega to element delete ho jayega.


#---------------------Driver Code:-------------------
if __name__ =="__main__":
     pass

LL=LinkedList()
LL.add_begin(10)
LL.add_end(30)
LL.add_begin(20)   
LL.add_after_node(78,20)  #78 ko 30 ke bad insert kra diya.
LL.delete_begin()
LL.add_before_node(45,30)  #45 ko 10 se phele insert kra diya.
LL.delete_end()
LL.delete_by_value(10)
LL.printLL()
















