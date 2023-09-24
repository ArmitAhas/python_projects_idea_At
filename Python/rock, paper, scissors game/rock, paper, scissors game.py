from random import randrange

name = input("What is your name? :")
print("this is rock, paper and scissors Game.")
print(" 1: rock \n 2: paper \n 3: Scissors")

g=0
p=0
i=0
while i<3 :
    gamer = int(input("Please choose an item!  "))
    i += 1
    item = {1: "rock", 2: "paper", 3: "scissors"}
    item2 = {1: "rock", 2: "paper", 3: "scissors"}

    rand = randrange(1, 3)
    a = print(item[gamer])
    b = print(item2[rand])

    if gamer==rand:
        print("you are equal !!!")
    elif gamer==1 and rand==3:
        print(name+" is winner!")
        g= g + 1
    elif   gamer==2 and rand==1:
        print(name+" is winner!")
        g = g + 1
    elif   gamer==3 and rand==2:
        print(name+" is winner!")
        g = g + 1
    else:
        print("PC is winner ;)")
        p=p+1

print(name+" "+"score is :",g )
print("Pc score is :",p)
if g>p :
    print(name+" "+"is winner!!")
elif p>g :
    print("PC is winner!!")
else :
    print("You are equal ")






