import py
p1=input("Enter the name of player1:")
p2=input("Enter the name of player2:")
opi=input("p1 do you want to continue playing?")
if(opi=="yes"):
   choice=rand.randint(11)
   luckydraw=rand.randint(11)
   if(choice==luckydraw):
      print("you won")
   else:
      print("sorry,you lost!")
   
