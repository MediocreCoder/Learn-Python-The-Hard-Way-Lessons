from sys import argv
script, filename = argv

print "Do you want open %r, write to it, and read it back?" % filename
raw_input('Press "ENTER" if YES\n\tOr\nCTRL-C(^C) to Quit')

print "OK, let's open %r using 'open(filename,'r+')'" % filename
textfile = open(filename, 'r+')
print "."*10 + "OPEN!"

print "Now, before we write, let's read this file real quick to know where we left off"
print "...FILE CONTENTS...\n\n"
print textfile.read(),
print "\n\n...END OF FILE CONTENTS..."

print "Looks good, care to .write() 2 more lines onto textfile?"
raw_input('Press "ENTER" if YES\n\tOr\nCTRL-C(^C) to Quit')

print "Add lines below!"
line1 = raw_input("ADD: ")
line2 = raw_input("ADD: ")
print "...Writing...Writing..."
textfile.write(
    """*%s\t(ADDED USING .write())
*%s\t(ADDED USING .write())\n""" % (line1, line2)
)

print "Dont writing! \nTo save we have to .close() and re .open()!\n"
textfile.close()

textfile = open(filename, 'r+')
print "\n That's enough for now, let's .read() back the updated file before we .close() it properly"
print "...FILE CONTENTS...\n\n"
print textfile.read(),
print "\n\n...END OF FILE CONTENTS..."

textfile.close()
