# https://takeuforward.org/practice/dsa/find-the-intersection-point-of-y-ll
# Problem: Given the heads of two linked lists A and B, containing positive integers. Find the node at which the two linked lists intersect. If they do intersect, 
# return the node at which the intersection begins, otherwise return null.
# The Linked List will not contain any cycles. The linked lists must retain their original structure, given as per the input, after the function returns.


class Solution:
    def getIntersectionNode(self, headA, headB):
        currentA = headA
        currentB = headB


        ## OPTIMISED APPROACH: traverse both linked lists. If any reaches the end, start with the head of the other linked list. When both points to the 
        # same point - that is the intersection point. If both becomes null together - it means there is no intersection
        while currentA and currentB:
            if currentA == currentB:
                return currentA
            currentA = currentA.next
            currentB = currentB.next

            if not currentA and not currentB:
                return None

            if not currentA:
                currentA = headB
            if not currentB:
                currentB = headA


        ## BRUTE FORCE: traverse and compare each node of both the linked lists
        # while currentA:
        #     while currentB:
        #         if currentB == currentA:
        #             return currentB
        #             currentB = currentB.next
        #     currentA = currentA.next
        # return None

# COMPLEXITIES
TIME: O(N)
SPACE: O(1)