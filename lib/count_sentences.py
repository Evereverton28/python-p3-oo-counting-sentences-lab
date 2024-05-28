#!/usr/bin/env python3

import sys
import io
import re

class MyString:
    def __init__(self, initial_value=""):
        self._value = ""
        if not isinstance(initial_value, str):
            print("The value must be a string.")
        else:
            self._value = initial_value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value
    
    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
        return self._value.endswith('?')
    
    def is_exclamation(self):
        return self._value.endswith('!')
    
    def count_sentences(self):
        sentences = re.split(r'[.?!](?=\s|$)', self._value)
        return len([sentence for sentence in sentences if sentence.strip()])

if __name__ == "__main__":
    my_string = MyString("Hello World. Is anybody there? It's me!")
    print(f"Count Sentences: {my_string.count_sentences()}")
    print(f"Is sentence: {my_string.is_sentence()}")
    print(f"Is question: {my_string.is_question()}")
    print(f"Is exclamation: {my_string.is_exclamation()}")
