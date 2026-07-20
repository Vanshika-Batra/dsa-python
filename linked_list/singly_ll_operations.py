# Question links:
# https://takeuforward.org/linked-list/insert-at-the-head-of-a-linked-list
# https://takeuforward.org/data-structure/delete-last-node-of-linked-list
# https://takeuforward.org/linked-list/find-the-length-of-a-linked-list
# https://takeuforward.org/linked-list/search-an-element-in-a-linked-list

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
        print("inserted element at the head...")
        self.display()

    def delete_tail(self):
        if not self.head or not self.head.next:
            print("EITHER NO LL OR SINGLE ELEMENT IS PRESENT")
            return None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            print("DELETED TAIL OF THE 1D LINKED LIST")
            self.display()
            return True

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, "->", end = "")
            curr = curr.next
    
    def length(self):
        total_nodes = 0
        if self.head:
            curr = self.head
            while curr:
                total_nodes += 1
                curr = curr.next
        return total_nodes

    def search(self, element):
        if self.head:
            curr = self.head
            while curr:
                if curr.data == element:
                    return True
                curr = curr.next
        return False


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(5)

    llist = LinkedList(head)
    llist.display()
    llist.insert_at_head(7)
    llist.delete_tail()
    llist.length()

    element = int(input("enter the element to be searched...: "))
    is_found = llist.search(element)
    if is_found:
        print(element, "is present in the list")
    else:
        print(element, "is missing in the list")

# COMPLEXITIES
# a) INSERTION AT THE HEAD ---> TIME - O(1), SPACE - O(1)
# b) DELETION OF THE TAIL ---> TIME - O(N), SPACE - O(1)
# c) FINDING LENGTH OF THE LIST ---> TIME - O(N), SPACE - O(1)
# d) FINDING GIVEN ELEMENT ---> TIME - O(N), SPACE - O(1)
# e) DISPLAYING LIST ELEMENTS ----> TIME - O(N), SPACE - O(1)