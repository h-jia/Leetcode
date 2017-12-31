
#enumerate同时扫描索引和值


nums = [2, 7, 11, 15]
target = 9
hash_map={}
for index, value in enumerate(nums):
    hash_map[value] = index #同时找出索引和值，注意顺序
    print(hash_map)
for index1, value in enumerate(nums):
    if target - value in hash_map:
       index2 = hash_map[target - value]
       if index1 !=index2:
            print(index1, index2)

