stack = []

stack.append(10)  # push
stack.append(20)
print(stack)

print(stack.pop())  # pop
print(stack[-1])    # peek: see the top element 

if (len(stack) == 0):
    print("Stack is empty")
else:
    print ("I think atleast one element is present")

class stack:
    def __init__(self):
        self.value = []
    def push (self, x):
        self.value.append(x)
    def pop(self):
        self.value.pop()
    def peek(self):
        return self.value[-1]
    def isempty(self):
        return len(self.value) == 0
        
s = stack()
s.push(10)
s.push(20)
s.push(30)

print(s.value)  #all 3 operations are of time complexity O(1)

# 1 VALID PARENTHESIS
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if ch == ')' and top != '(':
                    return False
                if ch == '}' and top != '{':
                    return False
                if ch == ']' and top != '[':
                    return False

        return len(stack) == 0

# min stack 
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.minstack) == 0:
            self.minstack.append(value)
        elif value <= self.minstack[-1]:
            self.minstack.append(value)

    def pop(self) -> None:
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
    

# MONOTONIC STACK
while stack and stack[-1] <= arr[i]:
    stack.pop()

#implement stack using queues
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0

#implement queue using stack
class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        self.peek()  # ensure outStack has elements
        return self.outStack.pop()

    def peek(self) -> int:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self) -> bool:
        return not self.inStack and not self.outStack




# STACK USING LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None   # head

    def push(self, x):
        newnode = Node(x)
        newnode.next = self.top
        self.top = newnode

    def pop(self):
        if self.top is None:
            return None   # stack empty
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def isEmpty(self):
        return self.top is None

    def printStack(self):
        curr = self.top
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


''' Q2. 
NEXT GREATER ELEMENT 
'''
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = []
        for num in nums1:
            greater = -1
            pos = nums2.index(num)
            for i in range(pos + 1, len(nums2)):
                if nums2[i] > num:
                    greater = nums2[i]
                    break
            result.append(greater)
        return result
    
# Q3. Next greater element 2: in this cicular array or linked list is given 
# Input: nums = [1,2,1]
# Output: [2,-1,2]

class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = []
        for i in range(n):
            greater = -1
            for j in range(1, n):
                idx = (i + j) % n
                if nums[idx] > nums[i]:
                    greater = nums[idx]
                    break
            ans.append(greater)
        return ans
    
