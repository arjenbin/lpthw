name = 'Arjen Bin'
age = 35
height = 180 #centimeters
weight = 65 #Kilograms
eyes = 'blue'
teeth = 'white'
hair = 'blond'

cmtoinch = 0.393700787
kgtopounds = 2.20462262

#Converter
def cmToInch(cm):
	global cmtoinch
	return cm * cmtoinch 

#Converter
def kgToPounds(kg):
	global kgtopounds
	return kg * kgtopounds 

print(f"Let's talk about {name}.")
print(f"He's {round(cmToInch(height))} inches tall.")
print(f"He's {round(kgToPounds(weight))} pounds heavy")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the {hair} coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")