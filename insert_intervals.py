import copy
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new=copy.deepcopy(intervals)
        new.append(newInterval)
        new=sorted(new,key=lambda x:x[0])
        if len(new) <=1:
           return new
        ans=[]
        ans.append(new[0])
        for i in (1,len(new)):
           prev=ans[-1]
           curr=new[i]
           if prev[1]>=curr[0]:
              prev[1]=max(prev[1],curr[1])
           else:
              ans.append(curr)
        return ans


def main():
   intervals = [[1,3],[6,9]]
   newInterval = [2,5]
   ob=Solution()
   print(ob.insert(intervals,newInterval))

  

if __name__ == '__main__':
  main()