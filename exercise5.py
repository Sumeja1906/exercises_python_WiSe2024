# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:46:24 2024

@author: s_saciri22
"""

def buchstaben_ändern(string, buchstabe): 
    string_lower = string.lower()
    
    for v in "aeiou":
        new_sentence = []
        
        for char in string_lower:
            if char == buchstabe:
                new_sentence.append(v)
            else:
                new_sentence.append(char)

        print("".join(new_sentence))


 # buchstaben_ändern("banana", "a")
 
buchstaben_ändern("Wie geht es Ihnen?", "e")
                