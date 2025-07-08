class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        idx=[]
        row=len(matrix)
        col=len(matrix[0])

        for i in range(row):
           for j in range(col):
              if matrix[i][j]==0:
                 idx.append([i,j])
        
        for ele in idx:
           r=ele[0]
           c=ele[1]
           for i in range(row):
              for j in range(col):
                 if i==r or j==c :
                    matrix[i][j]=0
        
        
def main():
  matrix= [[1,1,1],[1,0,1],[1,1,1]]
  obj=Solution()
  obj.setZeroes(matrix)
  print(matrix)

if __name__ == '__main__':
  main()