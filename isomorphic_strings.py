class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1={}
        hash2={}
        for i in range(len(s)):
            if s[i] not in hash1:
               hash1[s[i]]=i
            if t[i] not in hash2:
               hash2[t[i]]=i
            if hash1[s[i]] != hash2[t[i]]:
               return False
        
        return True
def main():
  s = "egg"
  t = "add"
  obj=Solution()
  print(obj.isIsomorphic(s,t))
  
if __name__ == '__main__':
  main()