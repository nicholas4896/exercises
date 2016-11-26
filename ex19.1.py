def hello():
    first_name = raw_input("What is your first name? > ")
    age = raw_input("How old are you? > ")
    print "\tHello %s, so you're %s old eh..." % (first_name, age)

    last_name = raw_input("What is your last name? > ")
    print "So your full name is %s %s, Interesting..." % (first_name, last_name)


hello()
