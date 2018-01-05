	

	temptdict = {}
	max = 0
	pointer = 0
	for index, value in enmerate(s):
		if value in temptdict: #检查给丁的dict(s)字符是否存在于新建的dict
			pointer = max[temptdict[value] + 1, pointer] #指针不能后移 如果存在更新指针位置， 
														 #跳转到有该值的最新的位置
		maxLen = max(index - pointer + 1, maxLen) #计算max的值
		temptdict[value] = index #更新新建的dict 一个个的加入
	return maxLen


{
	p:0，#初始为空，更新一个
	w:1，#更新到2
	k:3,
	e:4,
	w:5
}

index 	--> 0, p #原dict第一个字符到新tempdict去找，没找到
pointer --> 0 #初始时字典为空，之后一点点加入
max 	--> index - pointer + 1 = 1 #pointer更新后再算 长度:w
{0:"p"}

index 	--> 1, w #检查
pointer --> 0 #初始时字典为空，之后一点点加入
max 	--> index - pointer + 1 = 2 #pointer更新后再算 长度:pw
{0:"p",1:"w"}

index 	--> 2, w #发现新建字典存在
pointer --> 2 #更新到存在字符的下一位
max 	--> index - pointer + 1 = 1 #pointer更新后再算 找到重复所以小 长度:w
{0:"p",2:"w"}

index 	--> 3, k
pointer --> 2 #更新到存在字符的下一位
max 	--> index - pointer + 1 = 2 #pointer更新后再算
{0:"p",2:"w",3:"k"}

index 	--> 4, e
pointer --> 2 #更新到存在字符的下一位
max 	--> index - pointer + 1 = 3 #pointer更新后再算
{0:"p",2:"w",3:"k",4:"e"}

index 	--> 5, w
pointer --> 5 #更新到存在字符的下一位
max 	--> index - pointer + 1 = 1 #pointer更新后再算
{0:"p",2:"w",3:"k",4:"e"}
