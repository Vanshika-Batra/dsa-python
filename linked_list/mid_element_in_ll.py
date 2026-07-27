# Problem Statement: Given the head of a linked list of integers, determine the middle node of the linked list. 
# However, if the linked list has an even number of nodes, return the second middle node.

# link: https://takeuforward.org/data-structure/find-middle-element-in-a-linked-list

class Node:
    def __init__(self, data, next = None):
        self.next = next
        self.data = data

class SinglyLList:
    def __init__(self, head =None):
        self.head = head

    def middle_element(self):
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast =fast.next.next
        return slow

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    # head = None
    objllist = SinglyLList(head)
    mid = objllist.middle_element()
    if mid:
        print("mid: ", mid.data)
    else:
        print("no mid element")


# COMPLEXITIES
# TIME: O(N) --> N/2 in actual
# SPACE: O(1)