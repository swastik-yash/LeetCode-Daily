class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        neg=0
        n=len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j]<0:
                    neg+=1

        for i in range(n):
            for j in range(n):
                if matrix[i][j]<0:
                    matrix[i][j]*=-1

        if neg % 2!=0:
            min_i, min_j=0,0
            min_val=matrix[0][0]
            for i in range(n):
                for j in range(n):
                    if matrix[i][j]<min_val:
                        min_i,min_j=i,j
                        min_val=matrix[i][j]
            matrix[min_i][min_j]*=-1
        
        sum=0
        for i in range(n):
            for j in range(n):
                sum+=matrix[i][j]

        return sum