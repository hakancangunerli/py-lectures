name= input("What's your name?")
nationality= input("What's your nationality?")
religion= input("What's your religious belief?")
age=int(input("What's your age?"))
skin= input("What's your skin color?")

question = raw_input("what's your gender? m/f")
if question == "m":
 print name,"is a", age,"year old","male",religion,"who has", nationality,"with" , skin, "skin" 
if question == "f":
  print name,"is a", age,"year old","female", "who believes in",religion,"who is", nationality,"with" , skin, "skin" 