
from traceback import print_list


class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
       
 
class SinglyLinkedList:
  
    def __init__(self):
        self.head = None
        self.tail = None

    def listlenght(self):
      currentnode=self.head 
      lenght=0
      while currentnode is not None :
        lenght+=1
        currentnode=currentnode.next
      return lenght 
 
    def insert_node(self, node_data):
        node = Node(node_data)
 
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
 
        self.tail = node 
 
 
    def insertAt(self,data,Position) :
      newnode=Node(data)
      if Position <0 or Position > self.listlenght() :
        print("Invalid Position !")
        return
      currentnode=self.head 
      if Position == 0 :
        self.head=newnode 
        self.head.next= currentnode
        return 
      currentposition=0
      while True : 
        if currentposition == Position :
          previousnode.next=newnode
          newnode.next=currentnode
          break
        previousnode=currentnode
        currentnode=currentnode.next
        currentposition+=1
 
    def getdata(self) :
      target= self.listlenght()-2
      currentnode=self.head
      for i in range(target) :
        currentnode=currentnode.next   
      print(currentnode.data)
 
    def printlist(self):
      if self.head is None :
       print("Empty List !")
       return
      currentnode=self.head 
      while True  :
        if currentnode is None :
          break
        print(currentnode.data,end="-->")
        currentnode=currentnode.next 

   
 
list1=SinglyLinkedList()
list1.insert_node(2)
list1.insert_node("osama")
list1.insert_node(67)
list1.insert_node(False)
list1.insertAt(34,1)
list1.insert_node(99)
list1.insert_node(4)
list1.printlist()
print()
list1.getdata()

# q = 'osama'
# print(f"{q}")
# list1.printlist()