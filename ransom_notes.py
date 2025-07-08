class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l1=len(ransomNote)
        l2=len(magazine)
        if l1>l2:
           return False
        i=j=0
        while j<l2:
           idx1=0
           idx2=j
           while idx1<l1 and idx2<l2 and ransomNote[idx1]==magazine[idx2]:
              if idx1==l1-1:
                return True
              idx1+=1
              idx2+=1
           j+=1
        return False
        
             
def main():
  ransomNote = "ab", magazine = "bcd"
  obj=Solution()
  result = obj.canConstruct(ransomNote, magazine)
  print(result)  # Expected output: False

if __name__ == '__main__':
  main()