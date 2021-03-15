# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def display(self):
        node = self
        out = '[' + str(node.val)
        node = node.next
        while node is not None:
            out += ',' + str(node.val)
            node = node.next
        out += ']'
        print(out)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        x = l1
        y = l2
        curr = dummy
        carry = 0
        while x is not None or y is not None:
            a = 0
            b = 0
            if x is not None:
                a = x.val
            if y is not None:
                b = y.val
            sum = a + b + carry
            carry = sum // 10
            curr.next = ListNode(val=sum % 10)
            if x is not None:
                x = x.next
            if y is not None:
                y = y.next
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next


# Test:
z = ListNode(3)
y = ListNode(4, z)
x = ListNode(2, y)

c = ListNode(4)
b = ListNode(6, c)
a = ListNode(5, b)

sol = Solution()
result = sol.addTwoNumbers(l1=x, l2=a)
result.display()
# [2,4,3] + [5,6,4] -> [7,0,8]
