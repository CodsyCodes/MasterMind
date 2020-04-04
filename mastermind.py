# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
def gen_code():
    set_code = []
    for i in range(4):
        val = random.randint(0,9)
        set_code.append(val)
    return set_code
    
def input_code():
    code = input("Enter your four digit guess code: ")
    return code

def mastermind():
    
    genCode = gen_code()
    for i in range(10):
        result = ""
        inputCode = [int(c) for c in input_code()]
        if inputCode == genCode:
             print("You guessed it!",genCode)
             break
        for element in inputCode:
            if element in genCode:
                if inputCode.index(element) == genCode.index(element):
                    result+="R"
                else:
                    result+="Y"
            else:
                result+="B"
        print(result)
    else:    
        print("You ran out of trys!",genCode)    
        
mastermind()

        
                
    
    
    
