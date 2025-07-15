# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1,list2) :
        dummy=ListNode()
        ans=dummy
        idx1=list1
        idx2=list2

        while idx1 and idx2:
            if idx1.val < idx2.val:
                ans.next=idx1
                idx1=idx1.next
            else :
                ans.next=idx2
                idx2=idx2.next
            ans=ans.next
        if idx1:
            ans.next=idx1
        else:
            ans.next=idx2
        return dummy.next
def main():
   
    l1 = [2,4,3], l2 = [5,6,4]
    sol = Solution()
    print(sol.mergeTwoLists(l1,l2))  

if __name__ == '__main__':
  main()