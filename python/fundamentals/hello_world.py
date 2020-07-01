# 1. TASK: print "Hello World"
print( "Hello World")
# 2. print "Hello Rebecca!" with the name in a variable
name = "Noelle"
print( "Hello", name, "!" )	# with a comma
print( "Hello"+ name+ "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 7
print( "Hello", name , "!" )	# with a comma
print( "Hello"+ str(name) + "!" )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "toast with jelly"
fave_food2 = "coffee"
print( 'I love to eat {} and drink {}.' .format(fave_food1, fave_food2)) # with .format()
print( f"I love to eat {fave_food1} and drink {fave_food2}." ) # with an f string

x= "Hello my name is %s." % "Rebecca"
y="My Favorite number is %d." % 7
print(x,y)

name = "Rebecca"
num = 7
print("My name is %s. My favorite number is %d" % (name, num))



