# Lesson 1: Getting Started w/ Python + Programming

## Data

### Preamble 
Most of coding is accessing, displaying, and interacting with data / information. 


The most common of these are:
- String: A set of characters (usually you can think of these are words)
- Integer: A whole number
- Float: A number with decimal points
- Booleans: Whether something is True of False
- Lists: An ordered list of a different type (i.e. Numbers, Strings, even other lists). I.e. [Eggs, Milk, Cheese]
- Dictionaries: A key value store (Not ordered). Think of this as looking something up. I.e. if details about you was a dictionary -> the Key "Name" would be the Value "Andy". Values can be any other data type.
- None: A representation of nothing or the lack of data.

Information is games is often in this types. For example - in a top-down 2D game, your X and Y coordinates may be floats that represent where you are on the screen (which may stored in a Dictionary, or a List). Your character's name may be stored as a string. Whether the game has started may be a boolean. Your score may be an Integer.

Alot of this information can be stored by variables. Variables is basically giving something a name that you can refer to in code. This is because without it - you'd need to refer to the specific location where the data is stored (usually in memory i.e. RAM), which would be really really hard to write. (Basically what a variable is really doing is saying "Hey, this data is stored in Memory Slot 1, or Memory Slot 2" - which the computer looks up for you and grabs).

For example - I may name a variable **Name** and say it is equal to "Andy" (a string). In python this would be written like this.

```
Name = "Andy"
```

Then I can access that data - and perform manipulations. For example - if I wanted to print it to the terminal - I'd say this -> and the terminal would say "Andy"

```
print(Name)
```

In python - I could even change what that variable means over time. For example - the following code would print "Andy" first, then print "Trevor".

```
Name = "Andy"
print(Name)
Name = "Trevor"
print(Name)
```

What you may notice is that in the above example - I didn't explicitly tell the computer that the Name was a string. This is because Python is a "dynamically" typed. This means the types of data is determined when the code is run, and is based on the context clues you're giving the system. In other languages - this may be statically typed - where you have to more explicitly the computer what the type of the variable is.

### Practical Introduction of defining these types - Basic

Let's get started with some examples. Let's start with defining a few things that may be helpful in game. Let's do this exercise together - and start by making a Python file in your IDE. First open the "binding-of-andy" folder that you downloaded in VScode. Then - on the left side of the IDE - left click on "Lesson One - Data", and select "New File". Name the file "Andy_Example.py". Open this file by clicking on it.

Often times - in a game, who you're playing has a name. So let's define a variable with the name of the main character. Let's say the main character is "Andy". To do this - type in:

```
main_character_name = "Andy"
print(main_character_name)
```

In the first line of the example - you defined a variable named "main_character_name" and assigned it to "Andy" (which is a string, and can be denoted by the quotation marks). Then on the second line - you used a function (we'll go over those in more detail later) in python which "prints" whatever is inside it (in this case, it's the variable - "main_character_name" which is equal to "Andy") to the terminal. So you should see "Andy" in your terminal.

Now - let's start storing some descriptive information about Andy. We can say that his health = 100 (yay, he's unhurt!) and whether he is a human (suprisingly - he is). Also to round it up, let's have his X and Y coordinates, which are 10.1 and 20.2 respectively (this is a 2D game, otherwise we'd have Z too!).

So - try to add the following code to the file you made before under the code you wrote before.

```
health = 100
human = True
x = 10.1
y = 20.2
```

That is declaring:
- an integer (health) which can be identified because it is fully made of whole number (i.e. no decimals) AND is not put in quotations
- a boolean (human) which can be identified because it is either True or False (capitalization is important), and doesn't have quotations as well. 
- a float (x / y) which can be identified because it is fully made of numbers, but has a single "." mark - denoting it is not a whole number (and doesn't have quotations as well).

### Practical Introduction of defining these types - Dictionaries

However - you may have noticed that we're storing alot of information that sort of related to each other (i.e. all variables are about the main character - Andy), but we haven't packaged them together so they can be understood to be about the same thing or Object (FORESHADOWING!!!!). Because we don't need to order these pieces of information - a dictionary would be a perfect fit. So to do so - I might make a dictionary under a variable "main_character", with code that looks something like this.

```
main_character = {
    "name" : "Andy",
    "health" : 100,
    "x" : 10.1,
    "y" : 20.2
}
```

or because we named all those variables above - I could have set this up by typing the following

```
main_character = {
    "name" : main_character_name,
    "health" : health,
    "x" : x,
    "y" : y
}
```

Python can tell that this is a dictionary - because it has those curly brackets. Then within those curly brackets, each item is stored as a key/value pair. For example - the first key is "name" (note - keys are often strings, but can be any primitive type - like an integer, or a float. But they can't be a list/dict), and the value for that key is "Andy". Then each additional key/value pair has a comma seperating each pair from each other.

So let's print this dictionary, so we can see it. Please copy the main_character code above - and add it to the file you made earlier, and also add the following line

```
print(main_character)
```

Now - what if you want to know certain values about the main character? You can do this - by accessing each - "Key" by using the following syntax:

```
dictionary_variable[key]
```

So for example - if I wanted to print the main characters health - I'd type

```
print(main_character["health"])
```

But oh no! What if Andy gets hit by an arrow that takes 5 damage? What we could do in that case is change (or overwrite) Andy's health to a new value. The general syntax to do this is:

```
dictionary_variable[key] = new_value
```

So in this case - I might type:

```
main_character["health"] = 95
```

however, I'm lazy, and don't want to remember what Andy's health was before the arrow. So an easier way is the following

```
main_character["health"] = main_character["health"] - 5
```

Now, let's see what happened to health, by adding the above line - and printing the main character variable again

```
print(main_character).
```

You should see that the first time you printed main_character - Andy had 100 health, and the second time it was printed - Andy now has 95.

But oh no - what if we need to track a new piece of information - like Andy's Sexiness?!? Never fear - with dictionaries you can add new key/value pairs at any time (or delete them). The syntax to do so is

```
dictionary_variable[new_key] = new_value
```

So to track Andys sexiness - I might type in:

```
main_character["sexiness"] = 100
```

Now - lets see this work in action - by printing the main_character yet again. So add the following code to the file (and the above line about sexiness as well)

```
print(main_character)
```

Awesome! We should now see 3 iterations of Andy, one when we originally declared it, one when we updated his health, and one with sexiness added.

For the next example let's make another dictionary for a side character - Trevor. Please create the side_character variable that is a dictionary with all the same key"s as the main_character variable (but you can edit the values!)

If you get stuck at any point - the full lesson's code is in the example.py file in the same folder as this readme!

### Practical Introduction of defining these types - Lists

Awesome! But what is we want to store many of these related characters together 😲??!?

Well, it's a good thing we have lists! As mentioned before - lists are an ordered set of things. Let's make a list for all the characters! To do so - type the following in the terminal:

```
characters = [main_character, side_character]
print(characters)
```

Python was able to tell this was a list, because of the brackets surrounding the items. Now - because these items are ordered, we can access them by the index. The index represents the number of the item, starting at the number 0. So the in the above example - Andy is index 0, and Trevor is index 1. To access Trevor - I might type:

```
trevor = characters[1]
print(trevor)
```
or 
```
print(characters[1])
```

But lists aren't forever baby. So, we can add and remove items from the list too. Let's pretend trevor died. We could type:

```
characters.pop()
```
or 
```
characters.pop(1)
```

Both of these are valid - because my default - pop() will remove the last item from the list (which happens to be index = 1, which is from in the past example).

However, death isn't forever either baby - so we can add him right back. To do that - you can "append" him to the list, by typing

```
characters.append(side_character)
```

Now Trevor is back and action in the characters variable!

But yay! Now we've gone over the basics of data types. In the next iteration - we're going to go over the magical world of loops!