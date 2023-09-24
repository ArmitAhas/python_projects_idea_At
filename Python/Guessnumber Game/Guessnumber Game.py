from random import randint

print("This is a Game !")
print("You have 5 chance for guess number !")

x = randint(1, 11)
i = 0
while i<6:

  n = int(input("Your chance : "))
  i+=1
  if x > n :
        print("This is lower than my number !!")
  elif x == n :
      print("HOOOORRRAAAAA !!")
      break
  else:
    print("This is upper than my number !!")

  if i==5:
     print("You are LOSER ;)")
     break









