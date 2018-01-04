#在python中，一边循环一边计算的机制，称为生成器（Generator）——>节省内存，可用while或者def+yield。
#https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138681965108490cb4c13182e472f8d87830f13be6e88000
#链表详解：http://blog.csdn.net/redRnt/article/details/77542810



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):#__init__ is the constructor for a class. 
                          #The self parameter refers to the instance of the object (like this in C++).
        self.val = x      #data head node has no data?
        self.next = None  #pointer to next node the end node must be none so...
        
        #递归定义。每生成一个新的节点，就必然有一个指向下一个节点的指针生成。
        
        
        
    def myPrint(self):
        print(self.val)
        if self.next:
            self.next.myPrint()

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
########################################################################################################
        root = ListNode(0) #dummy node.插在链表前，作用是更新了链表后直接返回.next就是全新的链表。root data, return ListNode(), we can initial with any value
        result = root #root need be moved?
        carry = 0 #carry

    	#three things: add, be added, carry. the result need be changed
        while l1 or l2 or carry == 1:
            value = 0 #result for this bit
            if l1: # if first bit exists
                value += l1.val
                l1 = l1.next #move to next position
                print("value={0}".format(value), "l1={0}".format(l1))#, "l1.next=".format(l1.next))
            if l2:
                value += l2.val
                l2 = l2.next
                print("value={0}".format(value), "l1={0}".format(l1))#, "l1.next=".format(l1.next))
            value += carry # dangqian wei zhixuyao gewei
            print("carry={0}".format(carry))
            root.next = ListNode(value % 10) #dangqianwei zhineng shi yige gewei shiwei gei jinwei 
            print("root={0}".format(root))
            carry = value // 10 #equates to int(value/10)
            root = root.next
        return result.next #dummy node.next 返回更新后的链表
########################################################################################################

class ListNode(object):
    def __init__(self, x):    
        self.val = x
        self.next = None

def initList(array):
    root = ListNode(array[0])
    result = root
    for index, value in enumerate(array):
        if index > 0:
            root.next = ListNode(value)
            root = root.next
    return result

def printList(linkList):
    if linkList:
        print("[", end="")
        while linkList.next:
            print(linkList.val, end=", ")
            linkList = linkList.next
        print(linkList.val, end="]\n")
    else:
        print("[]")

def execute():
    l1=initList([2,3,4])
    l2=initList([3,5,7])
    sol = Solution()
    printList(sol.addTwoNumbers(l1, l2))

if __name__ == "__main__":
    execute()
