nums = [2, 7, 11, 15]
target = 9
hash_map={}
for index, value in enumerate(nums):
    hash_map[value] = index #find both index and value's position
    print(hash_map)
for index1, value in enumerate(nums):
    if target - value in hash_map:
       index2 = hash_map[target - value]
       if index1 !=index2:
            print(index1, index2)

