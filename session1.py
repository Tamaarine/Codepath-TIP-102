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
