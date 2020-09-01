import random
import datetime
 
colors = ["red","orange","yellow","green","blue","violet","purple"] #
foods = ["pizza","steak","hamburgers"]
moods = ["happy","sad","so-so"]
weather = ["sunny","cloudy","hot","mild","cold"]
 
while True:
   string = input("How can I help you? (or enter 'quit' to exit) ")
 
   if string.find("quit") >= 0:
      print("Thanks for playing!!")
      break
 
   elif string.find("name") >= 0:
      print("My name is Fred")
 
   elif string.find("today") >= 0 or string.find("day") >= 0 or string.find("date") >= 0 or string.find("time") >= 0:
      today = datetime.datetime.now()   # need to re-format this
      print("Today is",today)
 
   elif string.find("color") >= 0:
      print("My favorite color is",random.choice(colors))
 
   elif string.find("food") >= 0:
      print("My favorite food is",random.choice(foods))
 
   elif string.find("feeling") >= 0:
      print("I am feeling",random.choice(moods))
 
   elif string.find("weather") >= 0:
      print("The weather is",random.choice(weather))
 
   else:
      print("Sorry, I did not understand -- please try again...")