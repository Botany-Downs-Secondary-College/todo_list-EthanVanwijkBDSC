# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:19:45 2021

@author: Ethan Van Wijk
"""
question = ""
list = []
stage = 1
# defines variables and listsw

while stage == 1:
    num = int(input("choose a mode by entering a number:\n"" 1: add task\n"" 2: View list\n"" 3: exit \n""  :"))
    if num == 1:
        while question != "end":
            question = input("add items to the list by typeing them and type end to stop adding items: ")
        list.append(question)
    elif num == 2:
        print(list)
    elif num == 3:
        stage = 2
    else:
        print("that not a valid number")
# asks for list items

print(list)
print("the list is complete")

#ends code
