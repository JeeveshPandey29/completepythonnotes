# LINEAR SEARCH: search element one by one 

arr = [10, 20, 30, 40, 50]
target = 40

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index:", i)
        break
else:
    print("Not Found")     

'''
Best: O(1)
Worst: O(n)

'''

# BINARY SEARCH : Works only on sorted arrays. WORKS ON SORTED ARRAY.

arr = [10, 20, 30, 40, 50, 60]
target = 40

low = 0
high = len(arr) - 1
    
while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Found at index:", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not Found")

'''
Best: O(1)
Worst: O(log n)

8 elements
↓
4 elements
↓
2 elements
↓
1 element

n
n/2
n/4
n/8
...
1

n / 2^k = 1
2^k = n
k = log₂(n)

'''
'''


BUBBLE SORTING: Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value
largest element moves to end after every pass '''


arr = [5, 3, 8, 4, 2]

n = len(arr)

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

'''
SELECTION SORT: The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

'''

arr = [5, 3, 8, 4, 2]
n = len(arr)
for i in range(n):
    min_val = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_val]:
            min_val = j

    arr[i], arr[min_val] = arr[min_val], arr[i]

print(arr)


'''
INSERTION SORT: The Insertion Sort algorithm uses one part of the array to hold the 
sorted values, and the other part of the array to hold values that are not sorted yet. 
'''

arr = [5, 3, 8, 4, 2]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = key

print(arr)


'''
MERGE SORT: divide array into halves sort both halves and then merge them

'''
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [5,3,8,4,2]

print(merge_sort(arr))