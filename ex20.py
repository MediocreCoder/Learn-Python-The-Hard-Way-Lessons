from sys import argv

# Setup variables from sys
script, input_file = argv

# This function reads from beginning to the end of a file
def print_all(f):
    print f.read()

# This function returns the file back to the start, which is the .seek(0), .seek(-1) would start from the end
def rewind(f):
    f.seek(0)
    
# Finally, this function progresses line by line through the file, each time it is run!
def print_a_line(line_count, f):
    print line_count, f.readline()
    
# All functions SETUP! Let's open(input_file) and assign it
current_file = open(input_file)

print "First let's print the whole file:\n"

# Calls the first function print_all(), using the current_file variable
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# Calls the 2nd function which rewind the current_file variable, this would not be necessary if the first read was a direct call ;)
rewind(current_file)

print "Let's print three lines:"

# Last function, iterates manually through the lines of code, printing out each one at a time. 
# Progression is held WITHIN the variable itself, the adding of 1 each time is for creating a number list within the print of the function
current_line = 1
print_a_line(current_line, current_file)
# print_a_line(current_line, open(input_file))

#^ The octothorpes here are locking out a code which I've added. It shows the result of not assigning a file's contents to a variable 
# and instead uses direct calling. 
# NOTICE: It will keep reading LINE 1 since it opens everything again and again! ;) 
# So use assignments on files where necessary and .close() them when finished!

current_line += 1
print_a_line(current_line, current_file)
#print_a_line(current_line, open(input_file))

current_line += 1
print_a_line(current_line, current_file)
#print_a_line(current_line, open(input_file))

#This closes the file since we have it open and assigned to a variable, current_file
# however remember, direct calling, such as:
#print_a_line(current_line, open(input_file))
# does not keep the file's progression in memory which means with each iteration, progression through the file WILL BE LOST!!!
current_file.close()
