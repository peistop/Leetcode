"""
"""
class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        scores = []
        for op in ops:
            if op != "C" and op != "D" and op != "+":
                scores.append(int(op))
            if op == "C":
                scores.pop()
            if op == "D" and len(scores) > 0:
                scores.append(scores[-1] * 2)
            if op == "+" and len(scores) > 1:
                scores.append(scores[-1] + scores[-2])
            print(scores)
        return sum(scores)

print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))