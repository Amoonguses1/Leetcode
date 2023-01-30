from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode],
                    k: int) -> Optional[ListNode]:
        """Function to rotate the given linked list k times
            Args:
                head(Optional[ListNode]): linked list
                k(int): how many rotate linked list
            Returns:
                Optional[ListNode]: The rotated linked list
        """
        # the fastest and simple solution
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes
        if not isinstance(k, int) or k > 2 * (10**9) or k < 0:
            raise ValueError("k must be intger in the range [0,2*10**9]")

        """
        if head is None:
            return head

        length = 1
        count = head
        while count.next is not None:
            length += 1
            count = count.next
        count.next = head
        k %= length
        tempnode = head
        for _ in range(length-k-1):
            tempnode = tempnode.next
        answer = tempnode.next
        tempnode.next = None
        return answer
        """
        # two pointers
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes
        if head is None or head.next is None:
            return head

        length = 1
        count = head
        while count.next is not None:
            length += 1
            count = count.next
        k %= length
        if k == 0:
            return head

        count.next = head
        dummy = ListNode(0)
        dummyhead = dummy
        for i in range(k-1):
            dummy.next = ListNode(0)
            dummy = dummy.next
        dummy.next = head
        fast = dummyhead.next.next
        slow = dummyhead.next
        prev = dummyhead.next
        while fast != slow:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next.next
        prev.next = None
        return slow
