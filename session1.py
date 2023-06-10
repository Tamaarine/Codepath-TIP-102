# Problem 1
def valid_parenthesis(input):
    stack = []
    for bracket in input:
        if bracket in "([{":
            stack.append(bracket)
        else:
            if stack[-1] == "(" and bracket == ")" or stack[-1] == "[" and bracket == "]" or stack[-1] == "{" and bracket == "}":
                stack.pop()
            else:
                return False
    
    return True if len(stack) == 0 else False

print(valid_parenthesis("()()[]"))
print(valid_parenthesis("("))
print(valid_parenthesis("[][][{{{()}}}]"))

# Problem 2
import heapq
class KthLargest:
    
    def __init__(self, k, nums):
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap) # Remove the smallest number. This is min heap
        

    def add(self, val):
        heapq.heappush(self.heap, val)
        heapq.heappop(self.heap)
        
        return self.heap[0]

kl1 = KthLargest(4, [2, 3, 4, 5, 6])
print(kl1.add(10)) # Returns 4
print(kl1.add(12)) # Returns 5
print(kl1.add(13)) # returns 6
print(kl1.add(14)) # Returns 10

# Problem 3
from collections import deque
class RecentCounter:

    def __init__(self):
        # Initialize a queue
        self.queue = deque()

    def ping(self, t):
        self.queue.append(t)
        
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
print("Problem 3-------")
rc = RecentCounter()
print(rc.ping(2000))
print(rc.ping(2001))
print(rc.ping(2002))
print(rc.ping(5000))
print(rc.ping(5001))

# Problem 4
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) > 0:
            # This needs to be >= to allow the same min to be inserted into the stack
            if self.minStack[-1] >= val:
                self.minStack.append(val)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            val = self.stack.pop()
            if val == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.minStack[-1]

print("Problem 4---")
ms = MinStack()
ms.push(0)
ms.push(1)
ms.push(0)
ms.pop()
print(ms.getMin())
ms.pop()

# Problem 5
class MyQueue:

    def __init__(self):
        self.enqueueStack = []
        self.dequeueStack = []

    def push(self, x: int) -> None:
        if self.dequeueStack:
            # Currently in the dequeuestack. Swap over
            self.swap()
        self.enqueueStack.append(x)

    def pop(self) -> int:
        if self.enqueueStack:
            self.swap()
        if len(self.dequeueStack) > 0:
            return self.dequeueStack.pop()

    def peek(self) -> int:
        if self.dequeueStack and len(self.dequeueStack) > 0:
            return self.dequeueStack[-1]
        elif self.enqueueStack and len(self.enqueueStack) > 0:
            return self.enqueueStack[0]
        
        return -1

    def empty(self) -> bool:
        if self.dequeueStack or self.enqueueStack:
            return False
        return True
        
    def swap(self):
        if not self.enqueueStack:
            while self.dequeueStack:
                self.enqueueStack.append(self.dequeueStack.pop())
        else:
            while self.enqueueStack:
                self.dequeueStack.append(self.enqueueStack.pop())

print("Problem 5---")
que = MyQueue()
que.push(1)
que.push(2)
que.push(3)
que.push(4)
que.push(5)
print(que.enqueueStack)
que.pop()
que.pop()
print(que.dequeueStack)
print(que.peek())
print(que.empty())
que.pop()
que.pop()
que.pop()
print(que.empty())
print(que.peek())
