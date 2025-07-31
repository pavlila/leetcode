# O(m + n)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head

        while list1 is not None and list2 is not None:
            node = ListNode(0)
            
            if list1.val < list2.val:
                node.val = list1.val
                list1 = list1.next
            else:
                node.val = list2.val
                list2 = list2.next
                
            curr.next = node
            curr = curr.next

        while list1 is not None:
            node = ListNode(0)
            node.val = list1.val
            list1 = list1.next
            curr.next = node
            curr = curr.next

        while list2 is not None:
            node = ListNode(0)
            node.val = list2.val
            list2 = list2.next
            curr.next = node
            curr = curr.next

        return head.next