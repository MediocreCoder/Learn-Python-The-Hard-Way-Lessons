from sys import argv
# In sys (terminal atm), you call using $python ex16.py ex16_EraseWriteSave.txt
# If the file called (ex16_EraseWriteSave.txt) doesn't exist, no worries, it will be created automatically!
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^c)."
print "If you do want that, hit RETURN."

# NEW: Progress simply requies RETURN
raw_input("?")

print "Opening the file..."
# Like in ex15.py, we open() a file and assign it to a variable. HOWEVER, notice the 'w' allows writing to the file opened!NEW: open(,'w')
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# The .truncate() removes ALL contents of the file when left blank!
target.truncate()

print "Now I'm going to ask you for three lines."

# Define string variables using user input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# The .write(variable) will write() directly to the file opened!
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# This also saves changes to the file!
print "And finally, we close it."
target.close()
