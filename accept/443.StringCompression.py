"""
443. String Compression
https://leetcode.com/problems/string-compression/description/

Easy: 90.24%
Testcase Example: ["a","a","b","b","c","c","c"]

Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to 
the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new 
length of the array.

Follow up:
Could you solve it using only O(1) extra space?

Example 1:
Input: ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should 
be: ["a","2","b","2","c","3"]

Example 2:
Input: ["a"]
Output: Return 1, and the first 1 characters of the input array should 
be: ["a"]

Example 3:
Input: ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should 
be: ["a","b","1","2"].
"""

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) <= 1:
            return len(chars)
        
        write = 0
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                if count == 1:
                    chars[write] = chars[i-1]
                    write += 1
                else:
                    chars[write: write + 1 + len(str(count))] = [chars[i-1]] + [c for c in str(count)]
                    write += len(str(count)) + 1
                count = 1
        # last char
        if count == 1:
            chars[write] = chars[-1]
            write += 1
        else:
            chars[write: write + 1 + len(str(count))] = [chars[-1]] + [c for c in str(count)]
            write += len(str(count)) + 1
        
        return len(chars[0: write])

if __name__ == '__main__':
    solution = Solution()
    chars = ["a","a","b","b","c","c","c"]
    print(solution.compress(chars))
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b" ]
    print(solution.compress(chars))