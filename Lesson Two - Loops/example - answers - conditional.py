name_list = ["Trevor", "Andy", "Jared", "", "Patrick"]


# Answer to exercise 1
total = 0
counter = 0

while counter <= 100:
    total += counter
    counter += 1

print(total)


# Answer to exercise 2
not_seen_empty = True
counter = 0

while not_seen_empty:
    if name_list[counter] == "":
        not_seen_empty = False
    else:
        print(name_list[counter])

    counter += 1
