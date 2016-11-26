from sys import argv;from os.path import exists;script, from_file, to_file = argv
indata = open(from_file).read();raw_input("Continue?");out_file = open(to_file, 'w').write(indata);print "Done"

# Why no need to close leh?
# out_file.close()
