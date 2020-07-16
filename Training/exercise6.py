#Assign 10 to the variable "types of people"
types_of_people = 10
hilarious = True
#assign a formatted string to variable x
x = f"There are {types_of_people} types of people"

#assign the string "binary" to the variable 'binary'
binary = "binary"
#assign the string "don't" to the variable 'do_not'
do_not = "don't"
#assign a 'double' formatted string to variable y
y = f"those who know {binary} and those who {do_not}."

print(x)
print(y)

#print formatted strings
print(f"I said: {x}")
print(f"I also said: {y}")

#assign a string to Joke eval varaible. for some reason it needs the parentheses{} at the end...
joke_eval = "Isn't that joke so funny? {}"
joke_eval2 = "Isn't that joke so funny? {}"
print(joke_eval.format(hilarious))
print(joke_eval2.format(y+x))

degreesc = 15.45 + 230
degreesmessage = "It is {} degrees celcius here"
print(degreesmessage.format(degreesc))

w="This is the left side of..."
e="a string with a right side"

print(w+e)