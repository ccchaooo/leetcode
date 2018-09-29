# You are given two non-empty linked lists representing two non-negative integers.
#  The digits are stored in reverse order and each of their nodes contain a single digit.
#  Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):

        resultNode = None

        add = 0
        while True:
            if l1.val == -1:
                l1.val = 0
            if l2.val == -1:
                l2.val = 0
            tSum = (l1.val + l2.val + add) % 10
            add = (l1.val + l2.val + add) / 10
            listn = ListNode(tSum)
            if resultNode == None:
                resultNode = listn
                flagNode = resultNode
            else:
                flagNode.next = listn
                flagNode = flagNode.next

            if l1.next is not None:
                l1 = l1.next
            else:
                l1.val = -1

            if l2.next is not None:
                l2 = l2.next
            else:
                l2.val = -1
            if l1.val == -1 and l2.val == -1:
                break
            if add != 0:
                listn = ListNode(add)
                flagNode.next = listn

            return resultNode
