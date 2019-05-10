'''
Specifications LinkedList:
We need a class called myList

This class needs te be able to create a linked list where every object on the list has 2 attributes nl. data which contains the vakue and next which contains the next value.
The following functions need to be added to the class.

insert:
This function creates a new node in the beginning of the linked list needs only a value
If the function fails it should return a 0 if it succeeds it should return a 1

append:
This function creates a new node at the end of the linked list needs only a value
If the function fails it should return a 0 if it succeeds it should return a 1

delete:
This function deletes a node by value from the linked list
If the function fails it should return a 0 if it succeeds it should return a 1

toString:
This function prints the linked list to the screen
If the function fails it should return a 0 if it succeeds it should return a 1

atIndex:
This function prints the value at a given index within the length of the linked list
If the function fails it should return a Index out of bound if it succeeds it should print the value and return a 1

'''

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class myList:
    def __init__(self):
        self.head = None

    # Function to add newnode at the beginning
    def insert(self, data_in):
        try:
            NewNode = node(data_in)
            NewNode.next = self.head
            self.head = NewNode
            return 1
        except:
            return 0

    # Function to add newnode at the end
    def append(self, data_in):
        try:
            NewNode = node(data_in)
            if self.head is None:
                self.head = NewNode
                return
            last = self.head
            while (last.next):
                last = last.next
            last.next = NewNode
            return 1
        except:
            return 0

    # Function to remove node
    def delete(self, Removekey):
        try:
            HeadVal = self.head

            if (HeadVal is not None):
                if (HeadVal.data == Removekey):
                    self.head = HeadVal.next
                    HeadVal = None
                    return

            while (HeadVal is not None):
                if HeadVal.data == Removekey:
                    break
                prev = HeadVal
                HeadVal = HeadVal.next

            if (HeadVal == None):
                return 0

            prev.next = HeadVal.next
            return 1
        except:
            return 0

    # Function to print the linkedlist
    def toString(self):
        try:
            printval = self.head
            while (printval):
                print(printval.data),
                printval = printval.next
            return 1
        except:
            return 0

    def atIndex(self, data):

        cur_idx = 1
        cur_node = self.head
        while cur_idx < data:
            if cur_node.next != None:
                cur_node = cur_node.next
                cur_idx += 1
            else:
                return 0
        print(cur_node.data)
        return 1


# Unit tests

try:
    print("Begin class test")
    llist = myList()
    print("Class myList created")
except AssertionError as error:
    print(error)
    print("function linkedlist failed")
try:
    print("Begin insert test")
    print(llist.insert(1))
    print("End insert test")
except AssertionError as error:
    print(error)
    print("function add node at beginning failed")
llist.insert(2)
llist.insert(3)
llist.insert(4)
try:
    print("Begin append test")
    print(llist.append(5))
    print("End append test")
except AssertionError as error:
    print(error)
    print("function add node to the end failed")
    pass
try:
    print("Begin delete test")
    print(llist.delete(2))
    print("End delete test")
except AssertionError as error:
    print(error)
    print("function remove node failed")
try:
    print("Begin print test")
    print(llist.toString())
    print("End print test")
except AssertionError as error:
    print(error)
    print("function print linkedlist failed")
print("begin atIndex test")
print(llist.atIndex(5))
print(llist.atIndex(3))
print("End atIndex test")
