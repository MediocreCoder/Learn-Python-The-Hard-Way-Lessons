from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
print "Using ONE LINE!!!\nREADY???\tHit ENTER"
raw_input()


open(to_file, 'w').write(open(from_file).read())


print "Alright, all done in ONE LINE."

# Keep in mind, that while this looks very cool, it may not be very legible of directly implicit to other programmers
# Perhaps Looking cool VS Company efficiency.
