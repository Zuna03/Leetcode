class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        ans=[]
        start=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if start==nums[i-1]:
                    ans.append(str(start))
                else:
                    ans.append(str(start)+"->"+str(nums[i-1]))
                start=nums[i]
        if start==nums[-1]:
            ans.append(str(start))
        else:
            ans.append(str(start)+"->"+str(nums[-1]))
                
        return ans
def main():
   intervals = [0,1,2,4,5,7]
   ob=Solution()
   print(ob.summaryRanges(intervals))

  

if __name__ == '__main__':
  main()