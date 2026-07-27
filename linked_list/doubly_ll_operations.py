# question links:
# https://takeuforward.org/data-structure/insert-at-end-of-doubly-linked-list
# https://takeuforward.org/data-structure/delete-last-node-of-a-doubly-linked-list
# https://takeuforward.org/data-structure/reverse-a-doubly-linked-list

class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, head=None, tail = None):
        self.head = head
        self.tail=head

        while self.tail and self.tail.next:
            self.tail = self.tail.next

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        
    def delete_tail(self):
        if not self.head:
            return None

        if self.tail == self.head:
            self.head = self.tail = None
            return
        
        self.tail = self.tail.prev
        self.tail.next = None
        

    # def reverse(self):
    #     if not self.head:
    #         return None
    #     curr = self.head
    #     last = None
    #     while curr:
    #         curr.next, curr.prev = curr.prev, curr.next
    #         last = curr
    #         curr = curr.prev
    #     self.head = last
    #     self.display()


    def reverse(self):
        if not self.head:
            return

        curr = self.head

        # Old head becomes new tail
        self.tail = self.head

        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev

        # Old tail becomes new head
        self.head = self.tail
        while self.head.prev:
            self.head = self.head.prev


    def display(self):
        if not self.head:
            return None
        curr = self.head
        while curr:
            print(curr.data, end="")
            curr = curr.next
        print("")

if __name__ == "__main__":
    node = Node(5)
    node.next = Node(2)
    node.next.prev = node

    element = int(input("enter the element to be inserted: "))
    dllist = DoublyLinkedList(node)

    dllist.insert_at_end(element)
    dllist.display()

    dllist.delete_tail()
    dllist.display()

    dllist.reverse()
    dllist.display()

# #COMPLEXITIES
# 1) INSERTION AT END: TIME - O(1), SPACE - O(1)
# 2) DISPLAY: TIME - O(N), SPACE - O(N)
# 3) DELETE TAIL: TIME - O(1) ,SPACE - O(1)
# 4) REVERSE: TIME - O(N), SPACE - O(1)