# Definition for singly-linked list.
import copy

from typing_extensions import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        if head is None:
            return [ListNode(0, None)]

        i = copy.deepcopy(head)

        n = 0

        while i.next is not None:
            i = i.next
            n += 1

        counter = 0
        list_no = 1
        while head.next is not None:
            counter += 1

            if counter > (n / list_no) + (n % list_no):
                counter = 0
                list_no += 1


if __name__ == "__main__":
    s = Solution()
    s.splitListToParts()
