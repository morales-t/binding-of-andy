main_character_name = "Andy"
print(main_character_name)

health = 100
human = True
x = 10.1
y = 20.2

main_character = {
    "name" : main_character_name,
    "health" : health,
    "x" : x,
    "y" : y
}

# Andy is born!
print(main_character)

# Andy's health
print(main_character["health"])

main_character["health"] = main_character["health"] - 5

# Andy was hit by an arrow :(
print(main_character)

main_character["sexiness"] = 100

# Andy is now sexy!
print(main_character)

side_character = {
    "name" : "Trevor",
    "health" : 100,
    "x" : 11.1,
    "y" : 20.2,
    "sexiness" : 100000
}

characters = [main_character, side_character]

# List of characters
print(characters)

# Accessing Trevor
print(characters[1])

characters.pop()

# Trevor is gone
print(characters)

characters.append(side_character)

# Trevor is back
print(characters)
