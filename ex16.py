from sys import argv

x = "If you don't want that, hit CTRL-C (^C)."
y = "If you do want that, hit RETURN."

script, filename = argv

print "We're going to erase %r." % filename
print x
print y

# if CTRL C will stop the program, RETURN will continue
raw_input("?")

print "\tOpening the file... \n"
# setting variable to open filename ONLY
target = open(filename)
# reads the target
print target.read()
# closes it
target.close()

# double opt-in
print "Are you sure you want to erase %s?" % filename
print x
print y
raw_input("Confirm?")
# opens target again but in WRITE MODE
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file. \n"

target.write("%s\n%s\n%s") % (line1, line2, line3)
target.close()

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "\tHere is your new file"
target = open(filename)
print target.read()
print "And finally, we close it."
target.close()
