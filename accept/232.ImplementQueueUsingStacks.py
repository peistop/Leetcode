"""
232. Implement Queue using Stacks

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:

You must use only standard operations of a stack -- which means only 
push to top, peek/pop from top, size, and is empty operations are valid.
You may assume that all operations are valid (for example, no pop or 
peek operations will be called on an empty queue).
"""
class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.insert(0, x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.empty():
            return self.queue.pop()
        return None
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.empty():
            return self.queue[-1]
        return None
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0

if __name__ == "__main__":
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_1 = obj.peek()
    param_2 = obj.pop()
    param_3 = obj.empty()
    print(param_1, param_2, param_3)
