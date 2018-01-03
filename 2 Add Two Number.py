#在python中，一边循环一边计算的机制，称为生成器（Generator）——>节省内存




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):#__init__ is the constructor for a class. 
                          #The self parameter refers to the instance of the object (like this in C++).
        self.val = x      #data head node has no data?
        self.next = None  #pointer to next node the end node must be none so...
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
    
        root = ListNode(0) #root data, return ListNode(), we can initial with any value
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
        return result.next

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
