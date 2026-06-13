def find_item(data_list, target):
    for item in data_list:   #o(n)
        if item == target:   #O(1)
            return True
        return False
    
small_list = [10, 20, 30]
large_list = list(range(10000000))

print(30 in small_list)
print(99999 in large_list)