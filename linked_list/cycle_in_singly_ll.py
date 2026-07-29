# Floyd's Cycle Detection Algorithm
# Problem Statement: Given a Linked List, determine whether the linked list contains a cycle or not.

# link: https://takeuforward.org/data-structure/detect-a-cycle-in-a-linked-list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CycleDetection:
    def has_loop(self, head = None):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None


node = Node(5)
node.next = Node(3)
node.next.next = Node(5)
node.next.next.next = node

# node = None
ll = CycleDetection().has_loop(node)
if ll:
    print("Loop exists at: ", ll, ll.data)
else:
    print("There is no loop")


# #COMPLEXITIES
# TIME:   O(N)
# SPACE:  O(1)