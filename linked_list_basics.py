from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


# Create the linked list: 1 -> 1 -> 2
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)

solution = Solution()
result = solution.deleteDuplicates(head)

# Print the result
current = result
while current:
    print(current.val)
    current = current.next