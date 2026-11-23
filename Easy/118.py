class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        tri = [[1]] * numRows
        
        for i in range(1, numRows):
            tri[i] = [1]* (i+1)
            for v in range(1, i):
                
                tri[i][v] = (tri[i-1][v-1]+tri[i-1][v])
        return tri

#Array, Dynamic Programming, Pascal's Triangle