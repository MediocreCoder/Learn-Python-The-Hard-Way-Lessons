print "I will now count my chickens:"

print "Hens", 25.0 + 30.0 / 6.0 # Order of operation, python divides first BEFORE adding
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0 # Order of operation, python multiplies BEFORE modulus

print "Now I will count the eggs:"

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0 # 6.75   : Fraction recognized using floating point numbers VS all integers which produces a wrong answer of: 7due to ignoring the 1 / 4 among integers

print "Is it true that 3 + 2 < 5 - 7?"

print 3.0 + 2.0 < 5.0 - 7.0 # This is a True/False test using the "less-than" math operator

print "What is 3 + 2?", 3.0 + 2.0 # Spacing with commas on the same line
print "What is 5 - 7?", 5.0 - 7.0

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5.0 > -2.0
print "Is it greater or equal?", 5.0 >= -2.0
print "Is it less or equal?", 5.0 <= -2.0
