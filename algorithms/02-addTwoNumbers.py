#!/usr/bin/env python3

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def printList(self):
        print(self.val)
        if self.next != None:
            self.next.printList()
        else:
            return

class Solution:
    def __init__(self):
        self.list1 = []
        self.list2 = []

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.list1filler(l1)
        self.list2filler(l2)

        self.list1.reverse()
        self.list2.reverse()
        finalSum  = list(str(int("".join(map(str, self.list1))) + int("".join(map(str, self.list2)))))
        finalSum.reverse()
        return self.createListNode(finalSum)
            
        
    def createListNode(self, listParse: Optional[list[str]]) -> Optional[ListNode]:

            myList = ListNode(listParse[0])
            if(len(listParse) > 1):
                myList.next = self.createListNode(listParse[1:])
            return myList

        
    
    def list1filler(self, l1: Optional[ListNode]):
        if l1.next != None:
            self.list1.append(l1.val)
            self.list1filler(l1.next)
        else:
            self.list1.append(l1.val)

    def list2filler(self, l2: Optional[ListNode]):
        if l2.next != None:
            self.list2.append(l2.val)
            self.list2filler(l2.next)
        else:
            self.list2.append(l2.val)
            
def createListNodeTest(listParse: Optional[list[str]]) -> Optional[ListNode]:
    myList = ListNode(listParse[0])
    if(len(listParse) > 1):
        myList.next = createListNodeTest(listParse[1:])
    return myList
            
if __name__ == "__main__":
    t1 = ['2', '4', '3']
    t2 = ['5', '6', '4']
    test1 = createListNodeTest(t1)
    test2 = createListNodeTest(t2)
    test = Solution()
    result = test.addTwoNumbers(test1, test2)
    result.printList()
    