print "____________________________________"

print " Exercise 15 : Reading Files "

print "____________________________________"

from sys import argv

script, filename = argv

txt              = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename agian:"
file_again       = raw_input("> ")

txt_again        = open(file_again)

print txt_again.read()

