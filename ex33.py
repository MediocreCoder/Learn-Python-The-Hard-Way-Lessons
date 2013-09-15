numbers = []
def get_one_to_ten(numbers):
    i = 0
    
    #Should a while-loop never end, press CTRL-C to abort!
    while i < 10:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i += 1
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i
        
get_one_to_ten(numbers)
    
print "The numbers: "

for num in numbers:
    print num
