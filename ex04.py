cars = 100 # variables can be integers
space_in_a_car = 4.0 # variables can be "floating point" numbers
drivers = 30
passengers = 90
cars_not_driven = cars - drivers # Variables can be treated as numerical numbers
cars_driven = drivers # variables can equal variables
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available." # Sample Output: "There are 100 cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
