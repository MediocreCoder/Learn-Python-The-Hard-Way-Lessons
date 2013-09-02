# This on is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# This one takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
# This one take NO arguments
def print_none():
    print "I got nothin'."

# Finally our functions are readed to be 'called', 'used', 'run'
# Here is how you call a function: function_name(argument1, argument2)
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
