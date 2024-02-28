# strings in python
# Date : 22/02/2024
# Name : David musila

city = "nairobi"

print(city[0]) # n
print(city[1]) # a
print(city[2]) # i
print(city[3]) # r
print(city[4]) # o
print(city[-1]) # b
print(city[-2]) # i




#convert to uppercase
print(city)
print("\n") # prints a new line 
print(city.upper())
name = "David Musila"
print(name)
print(name.lower()) #converts string to lower case

town = "   Naivasha   "

print(town)
print("\t") # new tab 
print(town.strip())

# add two strings

f_name = "David"
s_name = "Musila"

full_name = f_name + s_name 

print(full_name)

# replacing a character

fruit = "orange"

print(fruit.replace("o","y"))

subject = "physical, Sciences"

print(subject.split(","))

age = 30
height = 1.2

print("I am{0}years old and{1} metre tall" . format(age,height))

activity = "dancing"
print("My hobby is %s" %(activity))
name = "David Musila"
print(len(name))

print(f"My full name is {name}")

# printing a float
height = 1.2334909
print("My height is %5.3f"%(height))

# printing an integer
age = 32
print("My age is %d"% (age))

school = "Engineering"
course = "Electrical"

print("I am studying {course} in the school of {school}" .format(course = "Medicine",school = "Human Sciences"))

#lists is an ordered collection of data 