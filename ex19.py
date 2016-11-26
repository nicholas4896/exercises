# defiing a function called cheese and crackers with the arguements cheese count adn boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses\n%d boxes of crackers!\nThat's enough for a party!\nGet a blanket.\n" % (cheese_count, boxes_of_crackers)


print "We can just give the function numbers directly:"
# passing arguements to the function, calling it by typing it's name
cheese_and_crackers(2, 4)

print "OR, we can use variables from our script:"
# define variables myself and pass it into the same function
amount_of_cheese = 10;amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 1000)
