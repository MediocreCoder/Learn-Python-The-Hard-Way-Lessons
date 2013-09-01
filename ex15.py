from sys import argv

# From sys, use the following argument variables
script, filename = argv

# the filename needs to first be open(), open(filename) and applied to an accessible variable. In this case: txt
txt = open(filename)

# Lets the user know the name of the filename we opened and applied to txt. and then uses the .read() function on txt to display filename's contents
print "Here's your file %r:" % filename
print txt.read()

# Always close
txt.close()


# Now instead of using sys to obtain the filename variable, the user is requested to raw_input the file
print "I'll also ask you to type it again:"
file_again = raw_input("> ")

# The name of that file needs to be open(), open(file_again), and applied to the variable: txt_again
txt_again = open(file_again)

# Finally, again, read the variable you assigned an open(file).
print txt_again.read()

#Always close
txt_again.close()
