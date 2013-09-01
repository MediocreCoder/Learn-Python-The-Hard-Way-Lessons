from sys import argv
from os.path import exists

# Now we have another variable added $python ex17.py ex17.py ex17_copy.txt
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
input = open(from_file)
indata = input.read()


print "The input file is %d bytes long" % len(indata)

# exists() creates a boolean True/False return, in this case True
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)


print "Alright, all done."

# Remember, .close() must be done to save and close BOTH open documents ONLY when assigned to a variable.
# This is because as long as the file is open and assigned to a variable, that variable is using resources!
# Direct calling however, such as "open(to_file, 'w').write(indata)", does not need to be .close()
output.close()
input.close()
