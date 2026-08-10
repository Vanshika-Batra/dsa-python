# Problem Statement: Given a linked list and an integer N, the task is to delete the Nth node 
# from the end of the linked list and print the updated linked list.

# link: https://takeuforward.org/data-structure/remove-n-th-node-from-the-end-of-a-linked-list



class Node:
    def __init__(self, data, next = None):
        self.next = next
        self.data = data

class SinglyLList:
    def __init__(self, head =None):
        self.head = head

    def total_nodes(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    # BRUTE FORCE --> traverse the whole list - fetch total nodes - then traverse till (total -N) nodes and delete the next node
    def delete_nth_node(self, n):
        count = 0
        if n <= 0:
            return
        total_nodes = self.total_nodes()
        print("total ", total_nodes)
        if n > total_nodes:
            return count

        # Delete head
        if n == total_nodes:
            self.head = self.head.next
            return

        curr = self.head
        while curr and count < (total_nodes - n -1):
            curr = curr.next
            count += 1
    
        curr.next = curr.next.next


    #OPTIMIZED -- slow and fast pointers. 
    # INITIALLY, SLOW = HEAD AND FAST - SLOW = N + 1, and then traverse the list till the end 
    # when fast ptr becomes null, the slow's next is the Nth node from the last which needs to be deleted
    def delete_nth_node_from_last(self,n):
        if n <= 0:
            return None
        slow = fast = self.head
        for _ in range(n+1):
            if fast:
                fast = fast.next
            else:
                self.head = self.head.next
                return None
        # print("fast.data: ", fast.data)

        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next


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
    objllist.delete_nth_node(4)
    
    objllist.display_list()
    mid = objllist.delete_nth_node_from_last(3)
    objllist.display_list()


# COMPLEXITIES
## BRUTE FORCE:
        # TIME: O(N) + O(N) --> O(N)
        # SPACE: O(1)
## OPTIMIZED: 
        # TIME: O(N)
        # SPACE:    O(1)
