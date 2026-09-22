# https://takeuforward.org/practice/dsa/find-the-starting-point-in-ll?ai=true
# Problem: Given the head of a singly linked list, the task is to find the starting point of a loop in the linked list if it exists. Return the starting node if a loop exists; otherwise, return null.
# A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. Internally, pos denotes the index (0-based) of the node from where the loop starts.
# Note that pos is not passed as a parameter.


class Solution:
    def hasLoop(self, head):
        if not head:
            return None
        
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow ==fast:
                return slow
        return None

    def findStartingPoint(self, head):
        if not head:
            return None
        
        loop_node = self.hasLoop(head)
        if not loop_node:
            return loop_node
        curr = head
        while curr != loop_node:
            curr = curr.next
            loop_node = loop_node.next
        return curr


# COMPLEXITIES
# TIME: O(N)  --> O(N) + O(N)
# SPACE : O(1)