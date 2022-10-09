# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            
            return False
        
        listArr = []
        
        while head:
            
            listArr.append(head.val)
            head = head.next
            
        return listArr == listArr[::-1]
        