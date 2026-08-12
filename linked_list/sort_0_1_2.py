# Problem: Given a linked list containing only 0's, 1's, and 2's, sort the linked list by rearranging the links (not by changing the data values).
# url: https://takeuforward.org/data-structure/sort-a-linked-list-of-0s-1s-and-2s-by-changing-links

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def sort_numbers(self):
        zerohead = zerotail = onehead = onetail = twohead = twotail = None
        curr = self.head
        while curr:
            if curr.data == 0:
                if not zerohead:
                    zerohead = zerotail = curr
                else:
                    zerotail.next = curr
                    zerotail = curr
            elif curr.data == 1:
                if not onehead:
                    onehead = onetail = curr
                else:
                    onetail.next = curr
                    onetail = curr
            else:
                if not twohead:
                    twohead = twotail = curr
                else:
                    twotail.next = curr
                    twotail = curr
            
            curr = curr.next    
        if not zerohead:
            if not onehead:
                if twohead:
                    twotail.next = None
                return twohead
            else:
                if twohead:
                    onetail.next = twohead
                    twotail.next = None
                return onehead
        else:
            if not onehead:
                if twohead:
                    zerotail.next = twohead
                    twotail.next = None
                return zerohead
            else:
                if twohead:
                    zerotail.next = onehead
                    onetail.next = twohead
                    twotail.next = None
                else:
                    zerotail.next = onehead
                    onetail.next = None
                return zerohead
                
    
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, "->", end = "")
            curr = curr.next
        print("")
    

if __name__ == '__main__':
    head = Node(2)
    head.next = Node(2)
    head.next.next = Node(1)
    head.next.next.next = Node(1)

    # head = None
    llist = LinkedList(head)
    llist.display()
    llist.head = llist.sort_numbers()
    llist.display()


#COMPLEXITIES
# TIME: O(N)
# SPACE:    O(1)