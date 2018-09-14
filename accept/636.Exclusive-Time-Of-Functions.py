"""
636. Exclusive Time of Functions

Given the running logs of n functions that are executed in a nonpreemptive 
single threaded CPU, find the exclusive time of these functions.

Each function has a unique id, start from 0 to n-1. A function may be called 
recursively or by another function.

A log is a string has this format : function_id:start_or_end:timestamp. 
For example, "0:start:0" means function 0 starts from the very beginning of 
time 0. "0:end:0" means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this 
function, the time spent by calling other functions should not be considered 
as this function's exclusive time. You should return the exclusive time of 
each function sorted by their function id.

Example 1:

Input:
n = 2
logs = 
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
Output:[3, 4]
Explanation:
Function 0 starts at time 0, then it executes 2 units of time and reaches 
the end of time 1. 
Now function 0 calls function 1, function 1 starts at time 2, executes 4 
units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus 
executes 1 unit of time. 
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 
totally execute 4 units of time.

Note:
1. Input logs will be sorted by timestamp, NOT log id.
2. Your output should be sorted by function id, which means the 0th 
element of your output corresponds to the exclusive time of function 0.
3. Two functions won't start or end at the same time.
"""
class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        dic = {str(key): 0 for key in range(n)}
        stack = []
        for i in range(len(logs)):
            idx, state, timestamp = logs[i].split(":")
            if stack:
                if state == "start":
                    dic[stack[-1]] += int(timestamp) - prev
                    stack.append(idx)
                    prev = int(timestamp)
                else:
                    dic[stack[-1]] += int(timestamp) - prev + 1
                    stack.pop()
                    prev = int(timestamp) + 1
            else:
                stack.append(idx)
                prev = int(timestamp)
                
        return [dic[i] for i in dic]

if __name__ == "__main__":
    sol = Solution()
    n = 2
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    print(sol.exclusiveTime(n, logs))