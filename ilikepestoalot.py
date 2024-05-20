ilikepesto = []
otherfoods = []
for num in range(8):
    food = input("What's your favourite food?")
    if food != "pesto":
        otherfoods.append(food)
    if food == "pesto":
        ilikepesto.append(food)
print(f"Pesto is loved by {len(ilikepesto)} people!")
for num in range(len(ilikepesto)):
    print ("I like pesto")
print("Other Foods:")
for notpesto in otherfoods:
    print(notpesto)