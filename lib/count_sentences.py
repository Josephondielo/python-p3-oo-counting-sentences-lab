#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
  
        if isinstance(value, str):
            self._value = value
        else:
            self._value = ""

 
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    
    def is_sentence(self):
        """Return True if value ends with a period."""
        return self.value.endswith(".")

    def is_question(self):
        """Return True if value ends with a question mark."""
        return self.value.endswith("?")

    def is_exclamation(self):
        """Return True if value ends with an exclamation mark."""
        return self.value.endswith("!")

    def count_sentences(self):
        """
        Return the number of sentences in value.
        Sentences are considered to end with ., !, or ?.
        """
        
        parts = re.split(r"[.!?]+", self.value)
       
        sentences = [s.strip() for s in parts if s.strip()]
        return len(sentences)
