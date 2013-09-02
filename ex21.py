# Introducing "return" within a function
# Return allows a function to present data that can be assigned or used in various ways.

def add(a, b):
    print "ADDING: %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING: %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING: %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING: %d / %d" % (a, b)
    return a / b
    
    
print "Let's do some math with just functions!"

# Since each function is "return"ing in this ex21, you can assign a function, with whatever desired values going into it, to a variable!
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# Using assigned variables for output
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?" # Got it! -4391

