"""
This exercise teaches us how to import functions from a file which we've created, like this one, and then direct it within Python.

TWO WAYS

$python
>>>import ex25
>>>sentence = "All good things come to those who wait."
>>>words = ex25.break_words(sentence) 
# The . (dot, period) symbol is how you tell python, 
#'Hey, inside ex25 there's a function called break_words and I want to run it."
>>>words
['All','good','things','come','to','those','who','wait.']
$

OR

$python
>>>from ex25 import * #imports everything from ex25 for native use
>>>sentence = "All good things come to those who wait."
>>>words = break_words(sentence)
# The . (dot, period) symbol is not used here because all functions have been imported to run natively
>>>words
['All','good','things','come','to','those','who','wait.']
$

"""

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
    
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
    
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
    
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
