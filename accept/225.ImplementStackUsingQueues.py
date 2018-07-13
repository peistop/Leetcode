"""
225. Implement Stack using Queues

Easy
Testcase Example: ["MyStack","push","push","top","pop","empty"]\n
[[],[1],[2],[],[],[]]

mplement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

Notes:

1. You must use only standard operations of a queue -- which means only push 
to back, peek/pop from front, size, and is empty operations are valid.
2. You may assume that all operations are valid (for example, no pop or top 
operations will be called on an empty stack).
"""
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()
        self.tmp_stack = deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        while len(self.stack):
            self.tmp_stack.append(self.stack.popleft())
        self.stack.append(x)
        while len(self.tmp_stack):
            self.stack.append(self.tmp_stack.popleft())
           

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.popleft()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not self.empty():
            return self.stack[0]
        else:
            return None
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0

if __name__ == "__main__":
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.top()
    param_3 = obj.pop()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)