from sys import argv
# setting variables script and filename
script, filename =argv
# defining txt as a variable that executes the open() command with the variable filename
txt = open(filename)
# prints filename
print "Here's your file %r:" % filename
# READS the file using .read() txt is open(filename), need open().read
print txt.read()

print "Type the filename again:"
# raw_inputing the filename but defined as file_again variable
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()

txt_again.close()
# can I combine open().read?
