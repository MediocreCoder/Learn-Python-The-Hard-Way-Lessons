animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

def cardinal(input_list, cardinal):
    return "The animal listed at cardinal %d is %s" % (cardinal, input_list[cardinal])

def ordinal(input_list, ordinal):
    return "The animal listed at ordinal %d is %s" % (ordinal, input_list[ordinal-1])
 
#This creates a for-loop which will call both the cardinal and ordinal functions
for card in range(0,5):
    print "%s\nSo...\n%s\n" % (cardinal(animals, card), ordinal(animals, card+1))
