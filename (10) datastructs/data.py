# dictionaries and list
{} # squiggly brackets, dictionary
[] # paranthesis, list 
() # tuples

# lists, dictionaries, tuples , sets 
a =["1","2","3"] # value 

a.append('4')
print(a)
tupled = tuple(a)
tupled.pop(2) # deletes index
print(tupled)
tupled.pop()
print(tupled) #last element

abc = {'hello':'a', 'oops' : 'hi', 'wassup' :'c' } # a key, and a value 
#print(abc)
#(abc['hello']) # if you mention key, it gets value 

#tuples immutable, mutable 
abd = ('123','456','789')
#abd.append('3')
print(abd)
# abd.pop()
print(abd)

tup1 = ("g","e","f") # you can add tuples NOT indexes, you cannot remove them,
tup2 = ("a",'b','c')
tup3= tup1 + tup2
