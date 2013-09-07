print """REVIEW for Exercises 1-21

PRINTING
print "Hello World"
>> Hello World
print "My dog's name is %s and he is %d years old. Can you say %r!" % ('Sam', 4, 'WOW')
>> My dog's name is Sam and he is 4 years old. Can you say 'WOW'! # Notice %r gives exact variable info!

VARIABLE TYPES AND DATA TYPES
my_int = 1 # integer
my_float = 1.234 # float
my_bool = True # boolean
my_str = 'word'
my_list = [1, 1.234, True, 'word'] # list
my_tuple = (1, 1.234, True, 'word') # tuple (immutable)
my_dict = {'name':'John','code':1.234,1:'A'} # dictionary, NOTICE key:variable)

    *BONUS* Use int() or str() to change variable types

ARITHMETIC OPERATORS
+   addition
-   subtraction
*   multiplication
/   division
**  exponentiation
%   modulus (Gives remainder, ex: 9%4 equals 1
//  floor division (divides and excludes remainder, ex: 9//4 equals 2

COMPARISON OPERATORS
==  equal
!=  not equal (may also use <>)
>   greater than
<   less than
>=  greater than or equal to
<=  less than or equal to

ASSIGNMENT OPERATORS
=   simple assignment,   c = a + b assigns a + b to c
+=  adds left and right and assigns result left,    c += a is the same as c = c + a
-=  *deduce*
*=
/=
%=
//=

HOW TO OPEN/READ/WRITE/CLOSE FILES (USING SAMPLE CODE ### to ###)

$python this-file-AKA-your-program.py file-to-effect.txt
from sys import argv

script, filename = argv

print "OPEN"
text_file = open(filename, 'r+')
print "READ..."
print "..."
print text_file.read()
print "..."
print "Write."
text_file.write("\n"+raw_input("What would you like to add to %r? >" % filename))
print "Close."
text_file.close() # This saves changes made and opens memory
print "Reprints updated file!"
print "..."
print open(filename).read()
print "..."
$

    *LINUX BONUS* 
    $cat filename.txt
        This will read the contents of any file 
        on linux or OSX, sorry windows! ;)

FUNCTIONS (USING SAMPLE CODE from $ to $)

$
print "First let's define our function"
def get_even_or_odd(x):
    print "Welcome to the get_even_or_odd() function,"
    print "This inside of any function has a block like this indented"
    print "The end of a function's code is the end of the block"
    print "You have entered: %d" % x
    if x % 2 != 0:
        print "The number %d is odd" % x
    else:
        print "The number %d is even" % x
    print "This is the end of the get_even_or_odd() function.\n" 
print "Now let's call/run/execute the function known as 'get_even_or_odd' which we defined below using the variable 4 as input"
get_even_or_odd(4) 
$

"""
