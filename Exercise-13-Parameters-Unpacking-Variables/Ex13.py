print "Exercise 13: Parameters, Unpacking, Variables"

print "_____________________________________________"

from sys import argv

script, first, second, third, name, job, company_name = argv

print "The scrip is called:", script
print "Your first  variable is:", first
print "Your second variable is:", second
print "Your third  variable is:", third

print "_____________________________________________"
print " Study Drills "

print "My name is        :", name         
print "My job is         :", job          
print "My Company Name is:", company_name 

print "_____________________________________________"

print "What is your name?         "
name         = raw_input()
print "What is your job?          "
job          = raw_input()
print "What is your company name? "
company_name = raw_input()

print "Hello, I am %r and I am working as a %r at %r." % (
	name, job, company_name)

print "_____________________________________________"

name         = raw_input("What is you name?")
job          = raw_input("What is your job?")
company_name = raw_input("What is your company name?")

print "Hello, I am %r and I am working as a %r at %r" % (
	name, job, company_name)