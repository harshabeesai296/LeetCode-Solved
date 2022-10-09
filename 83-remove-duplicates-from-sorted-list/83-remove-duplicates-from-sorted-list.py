# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def addNewNodes(self,val):
        
        newNode = ListNode(val)
        
        if self is None:
            
            self = newNode
            return
        
        lastNode = self
        
        while lastNode.next:
            
            lastNode = lastNode.next
            
        lastNode.next = newNode
        
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        listArray = []
        
        while head:
            
            listArray.append(head.val)
            head = head.next
            
        listArray = sorted(list(set(listArray)))
        finalList = ListNode()
        
        for elem in listArray:
            
            finalList.addNewNodes(elem)
            
        
        finalList = finalList.next
        
        return finalList
            
            
            
        