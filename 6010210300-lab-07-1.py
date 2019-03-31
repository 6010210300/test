"""Linked List lab
Incomplete implementation of a list ADT using a singly linked list."""
class SinglyLinkedList(object):
    """Singly Linked List Class"""

    class Node(object):
        """A nested storage class representing list nodes."""
        def __init__(self,item, next=None):
            """Instantiaties a Node with default next of Node"""
            self.data = item
            self.next = next

    def __init__(self):
        """Constructs an empty list"""
        self._head = None

    def insertBegin(self, item):
        """Adds a new item to the beginning (head) of the list."""

        if self._head is None:
            self._head = SinglyLinkedList.Node(item)
        else:
            newNode = SinglyLinkedList.Node(item)
            newNode.next = self._head
            self._head = newNode

    def visitNode(self):
        curNode = self._head
        while curNode is not None:
            print curNode.data,
            curNode = curNode.next
#------------------------------------------------------
#Unfinished methods
#------------------------------------------------------
    def append(self, item):
        """Adds a new item onto the end (tail) of the list."""

        if self._head is None:
            self._head = SinglyLinkedList.Node(item)
        else:
            newNode = SinglyLinkedList.Node(item)
            curNode = self._head
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next = newNode

    def count(self, target):
        """Returns a count of the number of times the given item is present in the list."""
        c = 0
        curNode = self._head
        while curNode is not None:
            if curNode.data == target:
                c = c+1                
            curNode = curNode.next
        return  c

    def index(self, target):
        """Returns the index of a target item in the list. Raise a value error if the item is not found"""
        try:
            # Display the result of finding here
            Index = 0
            curNode = self._head
            while curNode is not None:
                if curNode.data is target:
                    print ("Item %d is found at index " %target) + str(Index)
                    exit()
                Index = Index + 1
                curNode = curNode.next
            raise NotImplementedError("The target item is not in the list")
        except Exception as e:
            print e

#------------------------------------------------------

def main():

    #Create a list using adding new item at the beginning of the list
    import random

    list1 = SinglyLinkedList()
    for i in xrange(1,11):
        ran = random.randrange(1, 10)
        list1.insertBegin(ran)
    list1.visitNode()

    # Create a list using adding new item at the end of the list
    print ("\nInsert at the end")
    list2 = SinglyLinkedList()
    for j in xrange(1,11):
        ran2 = random.randrange(1, 10)
        list2.append(ran2)
    list2.visitNode()
    #---------------------------------------------------------

    # Count of the number of times the given item is present in the list
    print ("\nCount a number of times the given item is present")
    target = int(input("Enter a target number: "))
    # add your code here
    print list2.count(target)
    #---------------------------------------------------------

    # Find the index of target item in the list
    print ("\nFinding the index of target item in the list")
    target = int(input("Enter a target number: "))
    # add your code here
    list2.index(target)    
    # ---------------------------------------------------------


if __name__ == '__main__':
    main()
