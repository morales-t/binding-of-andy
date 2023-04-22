
cool_guys = ["Andy", "Patrick", "Trevor", "Jared"]
weapon = ["Gun", "Nunchuck", "Katana", "Bomb"]
characters = [
    {
        "name": "Jeff",
        "health": 20
    },
    {
        "name": "Trevor",
        "health": 10
    },
    {
        "name": "Jesus Christ",
        "health": 5
    },
    {
        "name": "Among Us",
        "health": 30
    },
    {
        "name": "Minecraft Steve",
        "health": 50
    },
    {
        "name": "Gorilla",
        "health": 70
    }
]

## Answer for 1:
for cool_guy in cool_guys:
    print(cool_guy)

## Answer for 2:
for name in cool_guys:
    for w in weapon:
        print(f"Name: {name}, Weapon: {w}")

## Answer for 3:
for c in characters:
    if c["name"] == "Trevor":
        c["health"] -= 5
    else:
        c["health"] += 5
    
print(characters)
