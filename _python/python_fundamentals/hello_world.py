# 1. Task: print "Hello World"
print("Hello World")

# 2a. Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a comma in the print function
name = "Eric"

print("Hello",name,"!")

# 2b. Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a + in the print function
name = "Eric"
print("Hello" + " " + name + "!")

# 3a. print "Hello 42!" with the number in a variable

num = 23
print("Hello", num, "!")

# 3b. Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a + in the print function (#3b)

num = 23
# print("Hello" + num + "!")
print("Hello" + " " + str(num) + "!")


# 4a. Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with the format method (#4a)
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))

# 4b. Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with f-strings (#4b)

print(f"I love to {fave_food1} and {fave_food2}")
print(f"I love to {fave_food1} and {fave_food2}".upper())
