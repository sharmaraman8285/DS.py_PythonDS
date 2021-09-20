#stack = A stack follows the LIFO (Last In First Out) principle, i.e., the element inserted at the last is the first element to come out.

# two method for implementing stack : 
# 1. collection --> deque
# 2. queue --> LifoQueue

  # not stack / len(stack) :-- show if their is any elements in the stack or not.
  # stack[-1] : show the element present at last / top of the stack.

  # Method 1 :using list -----------

# stack =[]
# def push_element():
#     elements = input("enter a number to add it into stack : ")
#     stack.append(elements)
#     print(stack)
# def pop_element():
#     if not stack:
#         print("Stack is empty")
#     else:
#         e = stack.pop()
#         print("removed ", e)
#         print(stack)

# while True:
#     print("select the operation : 1.Push , 2.Pop , 3.Quit ")
#     choice = int(input(""))
#     if choice==1:
#         push_element()
#     elif choice==2:
#         pop_element()
#     elif choice==3:
#         exit("Thank You for using Our stack Service")
#     else:
#         print("enter correct option to proceed")


  # Method 2 : using list some extra feature -----------


# stack =[]
# n=int(input("enter the size limit of stack : "))
# def push_element():
#     if len(stack) == n:
#         print("size of stack is reached ")
        
#     else:   
#         elements = input("enter a number to add it into stack : ")
#         stack.append(elements)
#         print(stack)
# def pop_element():
#     if not stack:
#         print("Stack is empty")
#     else:
#         e = stack.pop()
#         print("removed ", e)
#         print(stack)

# while True:
#     print("select the operation : 1.Push , 2.Pop , 3.Quit ")
#     choice = int(input(""))
#     if choice==1:
#         push_element()
#     elif choice==2:
#         pop_element()
#     elif choice==3:
#         exit("Thank You for using Our stack Service")
#     else:
#         print("enter correct option to proceed")


  # Method 3 :using deque -----------

# import collections  #import hota h stack ke liye.
# stack = collections.deque()  #empty stack create krte h is se.
# print(stack)  #stack print kr dega empty wali.
# stack.append(10)  # add 10 in stack.
# stack.append(20)
# stack.append(30)

# print(stack)  #print all added item in stack.

# stack.pop()  #last wala element pop kr dega. LIFO
# print("last wala delete krega sbse " , stack) # last wala pop krke baki print kr dega.
# stack.pop()
# print("bache hue me se last wala delete krega " , stack)


  # Method 4 :using LifoQueue -----------

# import queue
# stack = queue.LifoQueue()


# a=stack.put(10)  # put insert krne ke liye lagta h.
# a=stack.put(20)
# a=stack.put(30)
# a=stack.put(40)
# # print(a)  #ye insert krne ke baad show ni krta h. none dikhata h.
 
# a=stack.get()   #get pop krne ke liye lagta h.
# print(a) # pop krke hi print kra ra h ye

# a=stack.get()
# print(a) #pop krke hi print kra ra h ye





  # Method 4 : using LifoQueue , timeout  -----------

# import queue
# stack = queue.LifoQueue(3)  # stack ki limit set kr dega us se jyada dalenge to msg dega stack is full. or agar us ke sath timeout laga do to utne time ke bad dega msg.


# a=stack.put(10)  # put insert krne ke liye lagta h.
# a=stack.put(20)
# a=stack.put(30)
# a=stack.put(40,timeout=4)  # ab ye error dega 4 sec bad queue is full.
# # print(a)  #ye insert krne ke baad show ni krta h. none dikhata h.
 
# a=stack.get()   #get pop krne ke liye lagta h.
# print(a) # pop krke hi print kra ra h ye

# a=stack.get()
# print(a) #pop krke hi print kra ra h ye

# a=stack.get()
# print(a) 

# a=stack.get(timeout=5)  # agar ye 4th element pop krenge but limit 3 ki h stack me to timeout ke time ke bad error dega stack is queue is empty.
# print(a) 






