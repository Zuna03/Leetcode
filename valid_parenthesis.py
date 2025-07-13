from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        i=0
        for i in range(len(s)):
            if len(stack)!=0:
                top=stack[-1]
            ele=s[i]
            if len(stack)==0 or (top=='(' and ele !=')') or (top=='{' and ele !='}') or (top=='[' and ele !=']'):
                stack.append(ele)
            elif (top=='(' and ele ==')') or (top=='{' and ele =='}') or (top=='[' and ele ==']'):
                stack.pop()
        return True if len(stack)==0 else False
def main():
   s = "()[]{}"
   ob=Solution()
   print(ob.isValid(s))

  

if __name__ == '__main__':
  main()