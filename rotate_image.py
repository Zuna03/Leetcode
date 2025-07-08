class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()
def main():
#   matrix = [list(map(int, input().split())) for _ in range(int(input()))]
#   print(matrix)
  matrix = [[1,2,3],[4,5,6],[7,8,9]]
  obj=Solution()
  obj.rotate(matrix)
  print(matrix)


if __name__ == '__main__':
  main()