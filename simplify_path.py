from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts=path.split('/')
        stack=deque()

        for part in parts:
            if part=='' or part=='.':
                continue
            elif part=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        
        return '/' + '/'.join(stack)
def main():
   
   s="/home/user/Documents/../Pictures"
   ob=Solution()
   print(ob.simplifyPath(s))

  

if __name__ == '__main__':
  main()