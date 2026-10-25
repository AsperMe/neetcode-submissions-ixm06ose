class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left_Prev, cur = dummy, head

        for _ in range(left - 1):
            left_Prev, cur = cur, cur.next

        prev = None
        for _ in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        left_Prev.next.next = cur
        left_Prev.next = prev

        return dummy.next