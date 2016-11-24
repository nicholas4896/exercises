# defining x with a string with a %d which is calling 10
x = "There are %d types of people." % 10
# defining variable as string
binary = "binary"
# same
do_not = "don't"
# defining y as a string with %s, here %s has two values (binary, do_not) which themselves are variables previously defined as strings
# so it's possible to call a variable in with a formatter!!!! %s (var, var2, var 3)
y = "Those who know %s and those who %s." % (binary, do_not)
# print variable x
print x
# printing variable y
print y
# printing string with formatter %r calling x, a variable(string)
print "I said: %r." % x
# printing string with %s calling car y, a string with formatters calling variables
print "I also said: '%s'." % y
# defining variable as boolean
hilarious = False
# defining variable as string calling %r. Where does %r come from?
# why does it call hilarious and not from above %r. %x = string?
joke_evaluation = "Isn't that joke so funny?! %r"
# printing var + formatter variable
print joke_evaluation % hilarious
# defining w as string
w = "This is the left side of..."
# defining e as string
e = "a string with a right side."
# printing string + sting. string concatenation
print w + e

# %r = "raw" data
