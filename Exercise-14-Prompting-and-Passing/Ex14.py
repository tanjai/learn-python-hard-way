print "____________________________________"

print " Exercise 14 : Promting and Passing "

print "____________________________________"

from sys import argv

script, user_name, introduce, name = argv
promt            = '---> '

print " Hi %s I'm the %s script." % (user_name, script)
print " I'd like to ask you a few question. "
print " Do you like me %s? " % user_name
likes     = raw_input(promt)

print " Where do you live %s? " % user_name
lives     = raw_input(promt)

print " What kind of computer do you have? "
computer  = raw_input(promt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is. 
And you have a %r computer. Nice. 
""" % (likes, lives, computer)

print "____________________________________"
print " Study Drills "

print "Hello %s I am the %s script. " % (introduce, script)
print " I would like to introduce myself. "
print " My name is %s " % name
print " Can you repeat my name ? " 
repeat    = raw_input(promt)

print " I am working as a Test Analyst "
print " Can you tell me that what my job is "
job       = raw_input(promt)

print " My company is Asia Web Direct which is a part of Wotif Group "
print " Do you know my company ? "
know      = raw_input(promt)
print "Can you tell me the name of my company? "
company   = raw_input(promt)



print """
Let me introduce myself again
I am %r 
and I am working as a %r .
My company is %r . 
Thank you for listen my introduction. 
""" % (repeat, job, company)
