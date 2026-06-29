# A hashmap is a data structure that stores key-value pairs.

mp = {}                  # create empty hashmap
mp["apple"] = 5          # insert key-value
print(mp["apple"])       # access value → 5
print("apple" in mp)     # check if key exists → True
mp["apple"] = 10         # update value
del mp["apple"]          # delete key

# HASHMAP PATTERN
nums = [2, 7, 11, 15]
target = 9
mp = {}

for i in range(len(nums)):
    comp = target - nums[i]

    if comp in mp:
        return [mp[comp], i]

    mp[nums[i]] = i

# Q1.Two Sum Problem

mp = {}
for i, num in enumerate(nums):
    comp = target - num
    if comp in mp:
        return [mp[comp], i]
    mp[num] = i

# Q2. Counting Frequencies

s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)  # {'b':1, 'a':3, 'n':2}

# Q3. Avoiding Duplicates

nums = [1,2,3,1]
seen = {}
for num in nums:
    if num in seen:
        print("Duplicate:", num)
    seen[num] = True

# Q4. intersection of two arrays:  duplicates are allowed
'''
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        ans = []

        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        for num in nums2:
            if num in freq and freq[num] > 0:
                ans.append(num)
                freq[num] -= 1

        return ans

# Q5. intersection of 2 arrays: duplicates are not allowed: not hashmap approach 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
    

# SLOW FAST POINTER APPROACH 

k = 0   # slow pointer

for i in range(len(arr)):   # fast pointer
    if condition:           # check some condition on arr[i]
        arr[k] = arr[i]     # move valid element forward
        k += 1              # advance slow pointer


# Q1. remove duplicates 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k

# Q2. Move zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0: 
                nums[k], nums[i] = nums[i], nums[k]
                k+=1

        
#Q3. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

# Q4. sort array by parity moveeven integers at beginning 
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        k = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[k], nums[i] = nums[i], nums[k]
                k+= 1

        return nums

# Q5. Remove duplicates from sorted array: atmost 2 times one element you can keep
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k

# Q6. Mrge 2 sorted arrays: start from end 
class Solution:
    def merge(self, nums1, m, nums2, n):

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Q6. square of sorted array:  
''' 
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [0] * n

        left = 0
        right = n - 1
        k = n - 1

        while left <= right:

            if nums[left] * nums[left] > nums[right] * nums[right]:
                ans[k] = nums[left] * nums[left]
                left += 1
            else:
                ans[k] = nums[right] * nums[right]
                right -= 1

            k -= 1

        return ans
    
# Q7. duplicate zeroes
'''
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        temp = []

        for num in arr:

            if num == 0:
                temp.append(0)
                temp.append(0)

            else:
                temp.append(num)

        for i in range(len(arr)):
            arr[i] = temp[i]


# 2POINTER PROBLEMS: Both pointers move toward each other.

left = 0
right = len(nums) - 1

while left < right:
    ...


# Q1. Valid palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned += ch

        if cleaned == cleaned[::-1]:
            return True
        else:
            return False

# Q2. two sum input array is sorted 
class Solution:
    def twoSum(self, numbers, target):

        left = 0
        right = len(numbers) - 1

        while left < right:

            s = numbers[left] + numbers[right]

            if s == target:
                return [left + 1, right + 1]

            elif s < target:
                left += 1

            else:
                right -= 1

# Q3. Reverse a string 
'''
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        
# SLIDING WINDOW 
def max_sum_subarray(arr, k):
    # First window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        if window_sum > max_sum:
            max_sum = window_sum
    
    return max_sum

# Example
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9


# PREFIX SUM