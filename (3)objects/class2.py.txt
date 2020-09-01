class movie():
	def __init__ (self, name, rating, director, budget, description):
		self.name = name
		self.rating = rating
		self.director = director
		self.budget = budget
		self.description = description

toy_story = movie("ToyStory2" , 4 , "John Lasseter , Lee Unkrich , Ash Brannon" , "90 millon USD" , """When Woody is toy-napped by a greedy toy collector and is nowhere to be found, Buzz and his friends set out to rescue him.But Woody too is tempted by the idea of becoming immortal in a museum.
""")				  

print("Title : " + (toy_story.name))
print("Rating : " + str(toy_story.rating)) # bc it is a number
print("Director : " + (toy_story.director))
print("Budget : " + (toy_story.budget) + "\n")
print("Description :  " + (toy_story.description))
