formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.", 
    "That you could type up.", 
    "But it didn't sing", #the use of ' causes the %r output to use double quotes instead of single quotes
    'So I said "goodnight"'
)