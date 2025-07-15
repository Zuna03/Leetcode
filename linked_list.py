class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def append(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
    curr=self.head
    while curr.next:
      curr=curr.next
    curr.next=new_node
  def display(self):
    curr=self.head
    while curr:
      print(curr.data,end="->")
      curr=curr.next

def main():
  
    ll=Linkedlist()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()

if __name__ == '__main__':
  main()