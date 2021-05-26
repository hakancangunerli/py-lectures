

'''
# randomly generate a story where each part of the story are stored in a list 
import random
# when, who, what, went to
when = ['nightfall','sunrise','midmorning','afternoon','evening','midnight']
who = ['I','you','he','she','it']
what = ['to get presents', 'to walk their dog','to play with a rubik cube','to eat lunch']
went_to = ['the mall','a house of a friend', 'the park','the toy store','the cafe']

print('At ' + random.choice(when) + ', ' + random.choice(who) + ' wanted ' + random.choice(what) + ' and went to ' + random.choice(went_to))
'''
''''
#dice roller, random int while loop if the user n/no, then you should break the program 
import random
yes_decisions = ['Yes','yes','y','Of course','Duh']
no_decisions = ['No','no','n','nope']
i = input("Roll dice?") 
while i in yes_decisions:
  dice_roll = random.randint(1,6)
  print("your number is " + str(dice_roll))
  i = input("Roll again?")
  if i in no_decisions:
    print('Okay, bye!')
    break
  '''

# BMI = weight / (height/100)**2
''' 
BMI Categories:
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater
'''
weight = float(input('What is your weight? (kg)'))
height = float(input('What is your height? (cm)'))
BMI = weight / (height/100)**2
if BMI <= 18.5 :
  print('This is an underweight BMI.')
elif BMI in range(18.5, 24.9):
  print('This is a normal BMI.')
elif BMI in range(25,29.9):
  print('This is an overweight BMI.')
elif BMI >= 30:
  print('This is an obese BMI.')

we'll focus on other 