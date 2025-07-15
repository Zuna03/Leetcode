# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head) -> bool:
        if head is None or head.next is None:
            return False 
        slow=fast=head
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
def main():
  
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  
    sol = Solution()
    print(sol.hasCycle(node1))  

if __name__ == '__main__':
  main()

