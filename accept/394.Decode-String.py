"""
394. Decode String

"""
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(["", 1])
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            elif c == "[":
                stack.append(["", int(num)])
                num = ""
            elif c == "]":
                st, m = stack.pop()
                stack[-1][0] += st * m
            else:
                stack[-1][0] += c
        return stack[0][0]

if __name__ == "__main__":
    solution = Solution()
    s = "3[a]2[bc]"
    print(solution.decodeString(s))