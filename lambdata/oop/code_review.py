### IN style_example.py FILE###

import math,sys

def example1():
  some_tuple = (1, 2, 3, 'a')
  some_dictionary = {
      "long" : 'LONG CODE LINES should be wrapped within 79 character to prevent page cutoff stuff',
      'other': [math.pi, 100,200, 300, 9999292929292, "This IS a long string that looks gross and goes beyond what it should"],
      "more": {"inner": "THIS whole logical line should be wrapped"}, 
      "data": [444, 5555, 222, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5]
      }
  return (some_tuple, some_dictionary)

def example_2(): 
    return {"has_key() is deprecated" : True}

class Example:
    def __init__ (self, bar):
      self.bar = bar
    
    def bar_func (self, bar):      
        
        self.bar += 1
        self.bar = bar * bar   
        return self.bar
    
        else :
        some_string = "INDENTATION IN MULTIPLE STRINGS SHOULD NOT BE TOUCHED only actual code should be reindented THIS IS MORE CODE"
                
        return (sys.path, some_string)
