# Problem: Given the head of a singly linked list. Group all the nodes with odd values 
# followed by all the nodes with even values and return the reordered list. 
# Consider the 1st node to have index 1 and so on. The relative order of the elements inside the odd and even group must remain the same as the given input.


# link: https://takeuforward.org/data-structure/segregate-even-and-odd-nodes-in-linkedlist

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, "-->", end = "")
            curr = curr.next
        print("")
        return

    def segregate_odd_even(self):
        print("in segregate odd even")
        oddhead = evenhead = oddtail = eventail = None
        curr = self.head

        while curr:
            print("curr. data: ", curr.data)
            if curr.data % 2 == 0:
                print("is even")
                if not evenhead:
                    evenhead = eventail = curr
                else:
                    eventail.next = curr
                    eventail = curr
            else:
                if not oddhead:
                    oddhead = oddtail = curr
                else:
                    oddtail.next = curr
                    oddtail = curr
            curr = curr.next

        if not oddhead:
            print("no oddhead")
            return evenhead
        if not evenhead:
            print("no evenhead")
            return oddhead
        print("odd: ", oddhead.data)
        print("even: ", evenhead.data)
        eventail.next = oddhead
        oddtail.next = None
        return evenhead


if __name__ == '__main__':
    # head = None

    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(8)
    head.next.next.next.next.next = Node(0)

    llist = LinkedList(head)
    # llist.display()
    llist.head = llist.segregate_odd_even()
    llist.display()
    

#COMPLEXITIES
# TIME: O(N)  --> list is being traversed once
# SPACE: O(1) --> no extra space is being acquired

