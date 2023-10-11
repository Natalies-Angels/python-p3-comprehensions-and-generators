#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def make_exclamation(sentence_list):
   result = [sentence + "!" for sentence in sentence_list]
   return result
print(return_evens([10,9,7,6,5,4,3,2,1]))
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))

