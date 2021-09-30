#importing Heap module........

import heapq

# #initializing a empty binary heap tree as a list.........
# heap=[]

# #pushing elements in the heap..........
# heapq.heappush(heap,10)
# heapq.heappush(heap,30)
# heapq.heappush(heap,12)
# #printing the heap items..........
# print(heap)  #printing by following min heap properties.....

# #poping elements in the heap..........

# heapq.heappop(heap)   #pop out min elements, by following min heap properties.....
# heapq.heappop(heap)   

# #printing the heap items..........
# print(heap)  

#---------------------

#given a unordered list as a tree..............
heap=[3,9,10,12,45,23,68,6]

# #convert all types of unordered list into a min heap as a list...........
# heapq.heapify(heap)

# #printing the heap items..........
# print(heap)   #print by following min heap properties.....


# heapq.heappushpop(heap,11)  #pop the min element and insert the given element, by following min heap properties.....

# print(heap)


# heapq.heapreplace(heap,13)  ##push the element and pop the min element, by following min heap properties.....

# print(heap)



# print(heapq.nsmallest(2,heap))  #Print (2)smallest elements from the tree.......


# print(heapq.nlargest(3,heap))  #Print (3)largest elements from the tree.......














