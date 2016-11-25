from sys import argv

script, user_name, date = argv
prompt = '.' * 10

print "Hi %s, I'm the %s script, written on the %s" % (user_name, script, date)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

awesomeness = raw_input("Trump or Hilary? : ")

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
You're a %s lover ?!
""" % (likes, lives, computer, awesomeness)
