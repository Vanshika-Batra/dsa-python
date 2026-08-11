# Problem: Given the head of a linked list of integers, delete the middle node of the linked list and 
# return the modified head. However, if the linked list has an even number of nodes, delete the second middle node. 

# link: https://takeuforward.org/linked-list/delete-the-middle-node-of-the-linked-list

class Node:
    def __init__(self, data, next = None):
        self.next = next
        self.data = data

class SinglyLList:
    def __init__(self, head =None):
        self.head = head

    def remove_middle_node(self):
        if not self.head or not self.head.next:
            return None

        slow = fast = self.head
        temp = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
        
        if temp:
            temp.next = temp.next.next
        return


    def display_list(self):
        curr = self.head
        while curr:
            print(curr.data, " -> ", end="")
            curr = curr.next
        print("")

if __name__ == '__main__':
    head = Node(5)
    head.next = Node(4)
    head.next.next = Node(1)
    head.next.next.next = Node(0)

    # head = None
    objllist = SinglyLList(head)    
    objllist.display_list()
    is_deleted = objllist.remove_middle_node()
    if not is_deleted:
        print(is_deleted)
    else:
        objllist.display_list()


# # COMPLEXITIES
# TIME: O(N)
# SPACE:  O(1)
