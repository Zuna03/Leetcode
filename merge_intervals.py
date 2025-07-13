class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ans=[]
        if len(intervals)<=1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        ans=[intervals[0]]
        for i in range(1,len(intervals)):
            prev=ans[-1]
            curr=intervals[i]
            if curr[0]<=prev[1]:
                prev[1]=max(prev[1],curr[1])
            else:
                ans.append(curr)
        return ans
def main():
   intervals = [[1,3],[2,6],[8,10],[15,18]]
   ob=Solution()
   print(ob.merge(intervals))

  

if __name__ == '__main__':
  main()