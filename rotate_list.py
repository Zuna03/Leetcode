# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None or k==0:
            return head
        len=1
        curr=head
        
        while curr.next:
            len+=1
            curr=curr.next
        curr.next=head
        new_tail=head
        k=k%len
        for _ in range(len-k-1):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None

        return new_head
def main():
   
    l1 = [2,4,3]
    k=1
    sol = Solution()
    print(sol.rotateRight(l1,k))  

if __name__ == '__main__':
  main()


        