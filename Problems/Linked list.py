
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def reverse(self):
        self.tail = self.head
        prev, cur = None, self.head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev

    def listlenght(self):
        currentnode = self.head
        lenght = 0
        while currentnode is not None:
            lenght += 1
            currentnode = currentnode.next
        return lenght

    def insert_node(self, node_data):
        node = Node(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def insertAt(self, data, Position):
        newnode = Node(data)
        if Position < 0 or Position > self.listlenght():
            print("Invalid Position !")
            return
        currentnode = self.head
        if Position == 0:
            self.head = newnode
            self.head.next = currentnode
            return
        currentposition = 0
        while True:
            if currentposition == Position:
                previousnode.next = newnode
                newnode.next = currentnode
                break
            previousnode = currentnode
            currentnode = currentnode.next
            currentposition += 1

    def getdata(self):
        target = self.listlenght()-2
        currentnode = self.head
        for i in range(target):
            currentnode = currentnode.next
        print(currentnode.data)

    def printlist(self):
        if self.head is None:
            print("Empty List !")
            return
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data, end="-->")
            currentnode = currentnode.next

    def returnHead(self):
        return self.head

    def reverseBetween(self, left, right):
        counter = 1
        nodes = []      # to keep track of the nodes which needs to be reverse
        values = []       # to stores the values that needed to be reverse
        if not self.head.next and counter == 1:
            return self.head
        currentnode = self.head
        while currentnode:
            if counter >= left and counter <= right:
                values.append(currentnode.data)
                nodes.append(currentnode)
            counter += 1
            currentnode = currentnode.next
        for node in nodes:
            node.data = values.pop(-1)  # replace the value of nodes
        return self.head

    def quick_sort(self):
        listNodes = []
        cur = self.head
        while cur:
            listNodes.append(cur)
            cur = cur.next

        def rec(listNodes):
            if len(listNodes) < 2:
                return listNodes
            povit = listNodes[0]
            left = []
            right = []
            povits = []
            flag = True
            for item in listNodes:
                if item.data == povit.data and flag:
                    flag = False
                    continue
                elif item.data == povit.data:
                    povits.append(item)
                elif item.data < povit.data:
                    left.append(item)
                else:
                    right.append(item)
            povits.append(povit)
            return rec(left)+povits+rec(right)
        listNodes = rec(listNodes)
        self.head = listNodes[0]
        listNodes[-1].next = None
        for i, n in enumerate(listNodes):
            if i < len(listNodes)-1:
                listNodes[i].next = listNodes[i+1]
        return listNodes


list1 = SinglyLinkedList()
list1.insert_node(5)
list1.insert_node(9)
list1.insert_node(0)
list1.insert_node(-2)
# list1.insertAt(34, 1)
list1.insert_node(5)
# list1.insert_node(4)
# list1.insert_node(-2)
list1.printlist()
nodes = list1.quick_sort()

print()
for item in nodes:
    print(f"{item.data}-->", end='')
print()
# list1.getdata()
# list1.reverseBetween(2, 6)
list1.reverse()
list1.printlist()
# q = 'osama'
# print(f"{q}")
# list1.printlist()
