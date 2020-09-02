class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        
        if not head.next and (n==1 or n>1):
            return None
        
        last=head
        nth=None
        prev=None
        
        k=1
        f=0
        
        while last:
            
            if f==1:
                prev=nth
                nth=nth.next
            
            if k==n:
                prev=head
                nth=head
                f=1
            
            last=last.next
            k+=1
            
        if nth==prev:
            head=head.next
        else:
            prev.next=nth.next
        
        return head
