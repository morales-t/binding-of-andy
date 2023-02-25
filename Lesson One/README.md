# Lesson 1: Getting Started w/ Python + PyGame.

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

What you may notice is that in the above example - I didn't explicitly tell the computer that the Name was a string. This is because Python is a "Dynamically" typed. This means the types of data is determined when the code is run, and is based on the context clues you're giving the system. In other languages - this may be statically typed - where you have to more explicitly the computer what the type of the variable is.

### Practical Introduction of defining these types.

Let's get started with some examples 



