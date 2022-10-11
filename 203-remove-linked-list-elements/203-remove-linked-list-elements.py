# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def addNewNodeAtEnd(self,val):
        
        newNode = ListNode(val)
        
        if self is None:
            
            self = newNode
            return 
        
        lastNode = self
        
        while lastNode.next:
            
            lastNode = lastNode.next
            
        lastNode.next = newNode
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head is None:
            
            return head
        
        if head.next is None and head.val == val:
            
            newNode = ListNode()
            return newNode.next
        
        if head.next is None and head.val != val:
            
            return head
            
        listArr = []
        
        subHead = head
        
        while head:
            
            listArr.append(head.val)
            head = head.next
        
        print(listArr)
        
        if len(set(listArr)) == 1 and subHead.val == val:
            
            newNode = ListNode()
            return newNode.next
        
        if len(set(listArr)) == 1 and subHead.val != val:
            
            return subHead
            
#         for elem in listArr:
            
#             if elem == val:
                
#                 listArr.remove(val)
        
        listArrNonDup = [i for i in listArr if i != val]
        
        print(listArrNonDup)
        
        finalList = ListNode()
        
        for elem in listArrNonDup:
            
            finalList.addNewNodeAtEnd(elem)
            
        finalList = finalList.next
        
        return finalList
    
    