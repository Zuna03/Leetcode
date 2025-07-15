
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        dummy=ListNode()
        ans=dummy
        idx1=l1
        idx2=l2
        carry=0
        while idx1 or idx2 or carry:
            v1=idx1.val if idx1 else 0
            v2=idx2.val if idx2 else 0
            sum=v1+v2+carry
            value=sum%10
            carry=sum//10
                
            ans.next=ListNode(value)
            ans=ans.next
            if idx1:
                idx1=idx1.next
            if idx2:
                idx2=idx2.next
        return dummy.next
            
def main():
   
    l1 = [2,4,3], l2 = [5,6,4]
    sol = Solution()
    print(sol.addTwoNumbers(l1,l2))  

if __name__ == '__main__':
  main()