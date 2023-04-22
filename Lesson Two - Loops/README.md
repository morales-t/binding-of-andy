# Lesson two: Getting started with loops

## Loops

### Preamble 
One of the most powerful tools in programming are loops. A loop basically mean re-running a set of code over different (or the same) data for some amount of time.

For example - when you kick off a game - you are effectively creating a loop - where every millisecond (or faster) - your computer will look at various pieces of data for inputs (i.e. what key did you press or didn't press, where did you move your mouse) - process that information by running some code - and output a "Frame". So for one "frame" - your mouse may be at an X = 0, and Y = 0, then you move your mouse +10X and +20Y, and your cursor is now hovering over the "start game" button. Then the next second you click on the "start game button" so it starts the game (which is a new loop in of itself). Each iteration of taking your input - processing it - and providing an image in return can be a loop. Keep in mind - you can make loops on loops on loops.

When you think of loops - there are two main types. There's loops that are inherently finite over a set of items - and there's other loops that continue until a condition is true.

For example - a finite loop may be this: You're in a game - and you want to check the HP on each enemy to see if any died. Checking each enemy would be looping through the list (see data section if you forgot this), which would be finite to the number of items.

Alternatively - you may want to have a loop that outputs a frame forever until someone presses the "quit" button. This is a loop that will continue until the condition is met (i.e. in this case, the game status is set to QUIT).

### Practice

#### Finite looping over a set

Let's get started! Within python - the finite loop over a set is called a "For" loop. Basically the syntax is this:

```
for name_of_each_item in iterable:
    do_something
```

name_of_each_item in this case is arbitrary (and is basically naming a variable - that has one item in the iterable for each run of the loop). An iterable is a finite list of things that you can loop over. For example - a string is an iterable - where each iteration is each character in the string. Alternatively - the most common iterable is a list.

So for example - if I wrote the below code:

```
iterable = [1, 2, 3, 4]

for name_of_each_item in iterable:
    print(name_of_each_item)
```

The ouput would be:

```
1
2
3
4
```

this is because the loop will go through the iterable item, starting from the first element (or 0th element 😉) - put that in the "name_of_each_item" variable (which is arbitarily named - it can be anything) - and then executed the code within the loop. Though please note - if you're using a data structure that isn't inherently ordered (like a dictionary) the order will be effectively random.

So - it's time to get your hands dirty! Open up the file example_andy_use_me_pls.py. In there - I've defined a number of variables for you to use in the exercise. Then write code to do the following (note - I have answers in another file -so if you get very stuck - use that)

- Print the name of each character in the "cool_guys" variable
- For each combination of cool_guy and weapon - print the output as "Name: {name}, Weapon: {weapon}. SPECIAL NOTE: in python there is something called an f string. If you put an f before the quotations, you can directly inject the output of a variable in the text if you surround the variable name with curly bracket. For example - if I had a variable weapon = "Katana" and name = "Bob", and I typed print(f"Name: {name}, Weapon: {weapon}") it would output "Name: Bob, Weapon: Katana".
-  For each dictionary in the characters dictionary - subtract 5 health only if the character's name is Trevor. Otherwise add 5 health. Hint on how to do the "if" part below.

HINT:
to write code that only runs if a condition is true - the syntax is:

```
if boolean:
    code to run
else:
    code to run otherwise
```

Note: the else statement is optional. So an example of this would be:

```
if name == "Trevor":
    print("cool guy")
else:
    print("less cool guy")

```

Also note: If you are checking if something is equal to something - you have to use two equal signs. This is to explicitly tell python you're not trying to set a variable.

#### Conditional Loops

Within python, a conditional loop is a "while" loop. The syntax is:

```
while boolean:
    run code until boolean is false
```

This syntax is pretty straight forward! That said - tricky thing is that you have to be careful to make sure that the boolean eventually becomes false at some point. Otherwise, the loop will run forever, which is rarely what you want.

An example of good code is:

```
i = 0
while i < 5:
    print(i)
    i += 1
```

This code terminates - because i is incrementing upward until the question of i < 5 no longer becomes true (which is when i = 5). So this code would output

```
0
1
2
3
4
```

An example of bad code would be:

```
i = 0

while i >= 0:
    print(i)
    i += 1

```

This would run forever, because i will never be less than 0, and would likely give your computer a hard time.

That should be enough talking from me! Let's do some examples. Please open "example_andy_im_conditional_loop.py" and try to run the following with while loops:

- Use a while loop to add all numbers up to 100 together
- Use a while loop which will print each name in the list, but will stop when it reaches the empty string.

# CONGRATULATIONS - ANOTHER ONE IN THE BOOKS :D