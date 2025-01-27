from typing import List
from typing import Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]
                    ) -> Optional[ListNode]:
        """Function to merge k linked list
            Args:
                lists(List[Optional[ListNode]]): the list of
                    linked lists
            Returns:
                Optional[ListNode]: a merged linked list
        """
        # Time: O(totalnodes * log(listslen))
        # Space: O(totalnodes * log(listslen))
        # totalnodes is the total number of nodes in k linked lists
        # listslen = len(lists)
        """
        if not isinstance(lists, list):
            raise ValueError("lists must be list")

        for nodes in lists:
            if nodes != ListNode(0) and nodes is not None:
                raise ValueError("the element in lists must be linked list")

        length = len(lists)
        if length < 1:
            return

        if length == 1:
            return lists[0]

        if len(lists) > 2:
            mid = length // 2
            li = list()
            li.append(self.mergeKLists(lists[:mid]))
            li.append(self.mergeKLists(lists[mid:]))
            return self.mergeKLists(li)

        head = ListNode(0)
        dummy = head
        while lists[0] is not None and lists[1] is not None:
            if lists[0].val < lists[1].val:
                dummy.next = lists[0]
                lists[0] = lists[0].next
                dummy = dummy.next
            else:
                dummy.next = lists[1]
                lists[1] = lists[1].next
                dummy = dummy.next
        if lists[0] is not None:
            dummy.next = lists[0]
        if lists[1] is not None:
            dummy.next = lists[1]
        return head.next
        """
        # Time: O(totalnodes * log(listslen))
        # Space: O(totalnodes * log(listslen))
        # totalnodes is the total number of nodes in k linked lists
        # listslen = len(lists)
        li_val = []
        for nodes in lists:
            while nodes is not None:
                li_val.append(nodes.val)
                nodes = nodes.next
        heapq.heapify(li_val)
        head = ListNode(0)
        dummy = head
        while li_val:
            dummy.next = ListNode(heapq.heappop(li_val))
            dummy = dummy.next
        return head.next
