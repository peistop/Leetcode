"""

Easy: 97.56%

"""
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        res = [[1]]
        for i in range(1, numRows):
            tmp = [1]
            for j in range(1, i//2+1):
                tmp.append(res[i-1][j-1] + res[i-1][j])
            if i%2 == 1:
                tmp += tmp[0: i//2+1][::-1]
            else:
                tmp += tmp[0: i//2][::-1]
            res.append(tmp)
        return res

print(Solution().generate(6))