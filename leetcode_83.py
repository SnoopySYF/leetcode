# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None or head.next == None):
            return head
        last = head.val
        lnode = head
        node = head.next
        while(node != None):
            if(node.val == last):
                lnode.next = node.next
                node = lnode.next
            else:
                lnode = node
                node = lnode.next
                last = lnode.val
        return head

        