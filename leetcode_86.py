# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if(head == None or head.next == None):
            return head
        if(head.val < x):
            node2 = head
        else:
            node2 = None
        node1 = head.next
        Bnode1 = head
        while(node1):
            if(node1.val < x):
                if(Bnode1 == node2):
                    node2 = Bnode1 = node1
                    node1 = node1.next
                else:
                    if(node2):
                        Bnode1.next = node1.next
                        node1.next = node2.next
                        node2.next = node1
                        node2 = node1
                        node1 = Bnode1.next
                    else:
                        Bnode1.next = node1.next
                        node1.next = head
                        head = node1
                        node2 = head
                        node1 = Bnode1.next                    
            else:
                Bnode1 = node1
                node1 = node1.next
        return head

node1 = ListNode(1)
node1.next = node2 = ListNode(4)
node2.next = node3 = ListNode(3)
node3.next = node4 = ListNode(2)
node4.next = node5 = ListNode(5)
node5.next = node6 = ListNode(2)
s = Solution()
node = s.partition(node1, 3)
while(node):
    print(node.val)
    node = node.next

