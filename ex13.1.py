from sys import argv

script, author = argv

print "This is script %s, written by %s" % (script, author)

x = raw_input("\tWho is sexy? ")

print "Are you sure %s is sexy?" % x,

raw_input("Yes/No: ")

print "Well I think %s is sexier... just look at the code from %s!!!" % (author, script)

# can play around with the struture of the code, move prompt up/down
# to run this script I have to call its name hence printing ex13.1.
