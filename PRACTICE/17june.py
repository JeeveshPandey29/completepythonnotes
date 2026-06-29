# 1. max and min in an array

class MaxMinFinder:
    def __init__(self, arr):
        self.arr = arr

    def find(self):
        max_val = max(self.arr)
        min_val = min(self.arr)
        return {"Maximum": max_val, "Minimum": min_val}

obj1 = MaxMinFinder([5, 3, 9, 2, 8])
print(obj1.find())  


#2. second largest element
class SecondLargestFinder:
    def __init__(self, arr):
        self.arr = arr

    def second_largest(self):
        unique = list(set(self.arr))  
        unique.sort(reverse=True)
        return unique[1] if len(unique) > 1 else None

obj2 = SecondLargestFinder([7, 3, 9, 2, 8])
print(obj2.second_largest())

#3. remove duplicates from unsorted array 
class RD:
    def __init__(self, arr):
        self.arr = arr

    def remove_duplicates(self):
        return list(dict.fromkeys(self.arr))

obj3 = RD([3, 2, 3, 1, 2, 4])
print(obj3.remove_duplicates())   

#4. missing numbr:
class MNF:
    def __init__(self, arr):
        self.arr = arr

    def find_missing(self, n):
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(self.arr)
        return expected_sum - actual_sum

obj4 = MNF([0, 1, 3])
print(obj4.find_missing(3))  


#5 intersection of two array 
class ArrayIntersection:
    def __init__(self, arr):
        self.arr = arr

    def intersection(self, other):
        return list(set(self.arr) & set(other))

obj5 = ArrayIntersection([1, 2, 2, 1])
print(obj5.intersection([2, 2]))   # [2]

class ArrayRotation:
    def __init__(self, arr):
        self.arr = arr

    def rotate(self, k):
        k = k % len(self.arr)
        return self.arr[-k:] + self.arr[:-k]


# Example usage
obj6 = ArrayRotation([1, 2, 3, 4, 5])
print(obj6.rotate(2))   # [4, 5, 1, 2, 3]


class LargestZeroSumSubarray:
    def __init__(self, arr):
        self.arr = arr

    def find_subarray(self):
        prefix_sum = 0
        seen = {}
        max_len = 0
        start = end = -1
        for i, num in enumerate(self.arr):
            prefix_sum += num
            if prefix_sum == 0:
                max_len = i + 1
                start, end = 0, i
            if prefix_sum in seen:
                if i - seen[prefix_sum] > max_len:
                    max_len = i - seen[prefix_sum]
                    start, end = seen[prefix_sum] + 1, i
            else:
                seen[prefix_sum] = i
        return self.arr[start:end+1] if max_len > 0 else []


# Example usage
obj7 = LargestZeroSumSubarray([4, 2, -3, 1, 6])
print(obj7.find_subarray())   # [2, -3, 1]


class RearrangePosNeg:
    def __init__(self, arr):
        self.arr = arr

    def rearrange(self):
        pos = [x for x in self.arr if x >= 0]
        neg = [x for x in self.arr if x < 0]
        result = []
        i = j = 0
        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i += 1
            j += 1
        result.extend(pos[i:])
        result.extend(neg[j:])
        return result


# Example usage
obj8 = RearrangePosNeg([-1, 2, -3, 4, 5, -6])
print(obj8.rearrange())   # [2, -1, 4, -3, 5, -6]


class MajorityElementFinder:
    def __init__(self, arr):
        self.arr = arr

    def majority_element(self):
        candidate, count = None, 0
        for num in self.arr:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        if self.arr.count(candidate) > len(self.arr) // 2:
            return candidate
        return None


# Example usage
obj9 = MajorityElementFinder([3, 3, 4, 2, 4, 4, 2, 4, 4])
print(obj9.majority_element())   # 4


class ProductExceptSelf:
    def __init__(self, arr):
        self.arr = arr

    def product(self):
        n = len(self.arr)
        left = [1] * n
        right = [1] * n
        result = [1] * n

        for i in range(1, n):
            left[i] = left[i-1] * self.arr[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * self.arr[i+1]
        for i in range(n):
            result[i] = left[i] * right[i]
        return result


# Example usage
obj10 = ProductExceptSelf([1, 2, 3, 4])
print(obj10.product())   # [24, 12, 8, 6]
