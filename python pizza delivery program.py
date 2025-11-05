print("welcom to python pizza Deliveries!")
size=input("what size pizza do you want? S,M,L:")
pepperoni=input("do you want pepperoni on your pizza?yes or no:")
extra_cheese=input("do you want extra cheess ? yes or no:")
bill=0

if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("you type the wrong input.")

if pepperoni=="yes":
    if size=="S":
        bill+=2
    else:
        bill+=3

if extra_cheese=="yes":
    bill+=1

print(f"your final bill is:${bill}.")    
