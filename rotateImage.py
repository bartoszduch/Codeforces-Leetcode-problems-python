class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        tab=[]
        n=len(matrix)
        for i in range(n):
            for j in range(n):
                tab.append(matrix[i][j])
        k=0
        for i in range(n):
            for j in range(n):
                matrix[j][-i-1]=tab[k]
                k+=1
        return matrix
