# -*- coding:utf-8 -*-
import random
import sys
import re

random_number = random.randint(1,100)
count_list = ["First", "Second", "Third", "Fourth", "Fifth"]
print "Randomly generation number to 1 to 100."
print "Find for generated number at five attempt."
print "*Caution* Please input only number."

# Use Debug, Display random number.
#print random_number

# Main 
for count in count_list:
  print ""
  print count + " challenge!"
  print "Please input a number from 1 to 100"

  # validation input_number. allowed number only.
  while(True):
    input_number = raw_input('>>>  ')

    # Check input value.
    if re.match(r'[1-9]?[0-9]+',str(input_number)):
      break
    else:
      print str(input_number) + " is not number."
      print "Please input a number again."

  print "Input number is " + str(input_number)

  # decision 
  if random_number == int(input_number):
    print "Congratulations! Your correct match!"
    sys.exit()
  elif random_number < int(input_number):
    print "Too bad. Try a smaller number."
    print "Try again!"
  elif random_number > int(input_number):
    print "Too bad. Try a bigger nunber."
    print "Try again!"

# Failed Challenge
else:
  print ""
  print "Challenge failed."
  print "Correct number is " + str(random_number)
