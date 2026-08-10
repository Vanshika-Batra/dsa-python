# Problem: Given the head of a singly linked list representing a positive integer number. 
# Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. 
# Check whether the linked list values form a palindrome or not. Return true if it forms a palindrome, otherwise, return false. .
# A palindrome is a sequence that reads the same forward and backwards.

# link: https://takeuforward.org/data-structure/check-if-given-linked-list-is-plaindrome


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    

    # # BRUTE FORCE
    # def to_integer(self):
    #     curr = self.head
    #     integer = 0
    #     while curr:
    #         integer = integer*10 + curr.data
    #         curr = curr.next
    #     return integer
    
    # def is_palindrome(self):
    #     integer = self.to_integer()
    #     converted_integer = str(integer)
    #     return converted_integer == converted_integer[::-1], integer


    # OPTIMIZED APPROACH
    def reverse_second_half(self, start):
        curr = start
        prev = None
        while curr and curr.next:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        if curr and not curr.next:
            curr.next = prev
        return curr
        
    def find_middle_node(self):
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast and not fast.next:
                slow = slow.next
        return slow

    def display_list(self):
        curr = self.head
        while curr:
            print(curr.data, "--> ", end = "")
            curr = curr.next
        print("")

    def is_palindrome(self):
        if not self.head:
            return True
        mid = self.find_middle_node()
        second_half_head = self.reverse_second_half(mid)
    
        self.display_list()
        first_half_head = self.head

        while second_half_head:
            print(first_half_head.data, second_half_head.data)
            if first_half_head.data != second_half_head.data:
                return False
            second_half_head = second_half_head.next
            first_half_head = first_half_head.next
        return True

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

# head = None
ll = LinkedList(head).is_palindrome()
if ll:
    if head == None:
        number = None
    print(f"Is palindrome")
else:
    print(f"Is not Palindrome")


# COMPLEXITIES
# TIME: O(N)
# SPACE: O(N) --> for string of length n
