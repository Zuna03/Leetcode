import copy
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        copied=copy.deepcopy(board)
        row=len(board)
        col=len(board[0])
        for i in range(row):
           for j in range(col):
              cnt=0
              if i-1>=0 and j-1>=0 and copied[i-1][j-1]==1:
                 cnt+=1
              if i-1>=0 and j+1<col and copied[i-1][j+1]==1:
                 cnt+=1
              if i-1>=0 and copied[i-1][j]==1:
                 cnt+=1
              if j-1>=0 and copied[i][j-1]==1:
                 cnt+=1
              if j+1<col and copied[i][j+1]==1:
                 cnt+=1
              if i+1<row and j-1>=0 and copied[i+1][j-1]==1:
                 cnt+=1
              if i+1<row and j+1<col and copied[i+1][j+1]==1:
                 cnt+=1
              if i+1<row and copied[i+1][j]==1:
                 cnt+=1
              
              if copied[i][j]==1:
                 if cnt<2:
                    board[i][j]=0
                 if cnt>3:
                    board[i][j]=0
              if copied[i][j]==0:
                 if cnt==3:
                    board[i][j]=1
                 
            
             
                
                       

        
def main():
  matrix=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
  obj=Solution()
  obj.gameOfLife(matrix)
  print(matrix)

if __name__ == '__main__':
  main()