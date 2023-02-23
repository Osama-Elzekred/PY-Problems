
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        counter = 1
        nodes = []      # to keep track of the nodes which needs to be reverse
        values = []       # to stores the values that needed to be reverse
        if not head.next and counter == 1:
            return head
        currentnode = head
        while currentnode:
            if counter >= left and counter <= right:
                values.append(currentnode.val)
                nodes.append(currentnode)
            counter += 1
            currentnode = currentnode.next
        for node in nodes:
            node.val = values.pop(-1)  # replace the value of nodes
        return head
