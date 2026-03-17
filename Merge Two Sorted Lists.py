from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Recursive step
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# Helper function to convert a Python list to linked list
def list_to_linked(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Test the code
list1 = [1, 3, 5]
list2 = [4, 6, 7]

linked1 = list_to_linked(list1)
linked2 = list_to_linked(list2)

solution = Solution()
merged = solution.mergeTwoLists(linked1, linked2)

print("Merged Linked List:")
print_linked(merged)
