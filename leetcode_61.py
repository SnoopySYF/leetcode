class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if head == None:
            return head
        if head.next == None:
            return head
        node = head
        count = 0
        while(node):
            node = node.next
            count += 1
        k = k % count
        node = head
        while k:
            node = node.next
            k -= 1
            if(node == None):
                return head
        node2 = head
        while node.next:
            node2 = node2.next
            node = node.next
        node.next = head
        node = node2.next
        node2.next = None
        return node

node1 = ListNode(2)
node2 = ListNode(1)
node2.next = node1
print(Solution().rotateRight(node2,3).val)