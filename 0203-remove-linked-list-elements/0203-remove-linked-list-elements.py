# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head
        def remove_elm(curr,prev, val):
            if not curr:
                return curr
            if curr.val == val:
                # print('here')
                prev.next = curr.next if curr.next else None
                return remove_elm(curr.next, prev, val)
            else:
                # print('there')
                return remove_elm(curr.next, curr, val)
        remove_elm(sentinel.next, sentinel ,val)
        return sentinel.next