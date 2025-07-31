# string solution O(m + n)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""

        while l1:
            str1 += str(l1.val)
            l1 = l1.next
            
        while l2:
            str2 += str(l2.val)
            l2 = l2.next

        rstr1 = str1[::-1]
        rstr2 = str2[::-1]

        sm = int(rstr1) + int(rstr2)
        rsm = reversed(str(sm))

        res = ListNode(0)
        curr = res

        for val in rsm:
            curr.next = ListNode(int(val))
            curr = curr.next

        return res.next