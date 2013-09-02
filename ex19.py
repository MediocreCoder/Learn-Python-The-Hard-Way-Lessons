def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)


# Below is a function of my own design which will be run 10 different ways.
def make_partners(person1,person2):
    print "%s and %s will both be working together!" % (person1, person2)
    
# The 10 different ways!   
make_partners('John', 'Sally')
make_partners('T-Rex', 'Godzilla')
make_partners('Bonnie', 'Clyde')
make_partners('Cat', 'Dog')
make_partners('Americe', 'Canada')
make_partners('Mustard', 'Cheese')
make_partners('The lead guitar', 'vocals')
make_partners('My left foot', 'my right foot')
make_partners('Light', 'Dark')
make_partners('Thieves', 'Pirates')
make_partners('The Jr. Developer', 'The Boss')
