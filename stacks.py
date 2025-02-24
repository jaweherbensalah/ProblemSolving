"""Data structure tutorial exercise: Stack
1. 
Write a function in python that can reverse a string using stack data structure.
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
"""

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

def reverse_string(s):
    st=Stack()
    rstr=""
    for i in s:
        st.push(i)
        
    # print(st.container)

    while st.size():
        rstr+=st.pop()
    return rstr

        

print(reverse_string("We will conquere COVID-19"))
# return "91-DIVOC ereuqnoc lliw eW"

"""
2.
Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". 

is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
"""

def is_balanced(s):
    d = {")":"(","}":"{","]":"["}
    st=[]
    for i in s:
        if i not in d:
            st.append(i)
        else:
            popped=st.pop()
            if popped!=d[i]:
                return False
    
    return not st
    
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
print(is_balanced("({})"))