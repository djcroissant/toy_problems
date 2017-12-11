# Definition for singly-linked list.
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node = next_node

class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def __str__(self):
        lst = []
        node = self.head
        while not node.data == None:
            lst.append(node.data)
            node = node.next
        return lst


class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=False):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Assumptions:
            * l1 and l2 are non-empty
            * numbers are non-negative
            * digits stored in reverse order

        Test Case:
            Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
            Output: (7 -> 0 -> 8)
            Explanation: 342 + 465 = 807
        """
        num1 = l1.head.data
        num2 = l2.head.data

        if num1 and num2 == None:
            # Catch base case for recursive call
            if carry == True:
                sum_node.data = 1
                sum_node.next = None
            else:
                return None
        elif num1 == None:
            num1 = 0
        elif num2 == None:
            num2 = 0

        num_sum = num1 + num2

        if carry == True:
            # carry set by previous call
            num_sum += 1

        if num_sum >= 10:
            # Set carry for next call
            carry = True

        num_sum = num_sum % 10
        new_l1 = LinkedList(l1.head.next_node)
        new_l2 = LinkedList(l2.head.next_node)

        new_node = Node(num_sum, self.addTwoNumbers(new_l1, new_l2))

        return LinkedList(new_node)






sol = Solution()
l1 = LinkedList(Node(2, Node(4, Node(3, None))))
l2 = LinkedList(Node(4, Node(6, Node(5, None))))

sum_list = sol.addTwoNumbers(l1, l2)

print(sum_list)
