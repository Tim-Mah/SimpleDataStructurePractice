'''
@Auther: Tim Mah
Date: 2022

My implementation of a Stack class and a simple
object that uses Stack

An object of type Node holds one of the items
in the linked list that represents the stack.
'''
class Node:
    def __init__(self):
        self.link = None
        self.info = 0

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

            
    '''
    Checks if the stack is empty. 
    @return true if the stack is empty and false otherwise
    '''
    def isEmpty(self):
        if(self.top == None):
            return true
        return false

    '''
    Add a new element (n) to the top of the Stack. 
    @param n Integer to be added
    '''
        
    def push(self, n):
        self.size += 1
        temp = Node()
        temp.info = n;
        temp.link = self.top;
        self.top = temp

    '''
    Remove the top item from the stack and return it.
    @return The top element
    '''
    def pop(self):
        if(self.top != None):
            self.size = self.size -1
        popped_info = self.top.info;
        self.top = self.top.link;
        return popped_info;	
            
    def peek(self):
        return self.top.info;
            
    def size(self):
        return self.size;
# End stack class

def a(_data_items):
    prev_sum = _data_items.top.info + _data_items.top.link.info
    _data_items.push(prev_sum)
# end A

def t(_data_items):
    _data_items.push(_data_items.peek() * 3)
# end T

def d(_data_items):
    _data_items.pop()
# end D

class bot:
    def __init__(self, input_list):
        self.input_list = input_list
        self._data_items = Stack()

    def print_output(self):
        for i in range(len(self.input_list)):
            if self.input_list[i] == "a" or self.input_list[i] == "A":
                a(self._data_items)
            elif self.input_list[i] == "t" or self.input_list[i] == "T":
                t(self._data_items)
            elif self.input_list[i] == "d" or self.input_list[i] == "D":
                d(self._data_items)
            else:
                self._data_items.push(int(self.input_list[i]))

        this_node = self._data_items.top
        print("Top of the stack prints first")

        while(this_node != None):
            print(this_node.info,' ' ,end='')
            this_node = this_node.link
    # end function

# end bot

my_inputs = ["6", "9", "D", "T", "12", "A", "T", "2", "12"]
test_bot = bot(my_inputs)
test_bot.print_output()
