#snake water gun
import random
def game(input1,input2):
    if input1==input2:
        return None
    elif input1=='s':
        if input2=='w':
            return False
        elif input2=='g':
            return True
        else:
            return "invalid"
    elif input1=='w':
        if input2=='s':
            return True
        elif input2=='g':
            return False
        else:
            return "invalid"
    elif input1=='g':
        if input2=='w':
            return True
        elif input2=='s':
            return False
        else:
            return "invalid"
    
print("Computer's Turn: snake(s) water(w) or gun(g)")
r=random.randint(1,3)
if r==1:
    input1="s"
elif r==2:
    input1="w"
else :
    input1="g"
print("PLayer's Turn: ")
input2=input("enter snake(s) water(w) or gun(g):")
a=game(input1,input2)
print(f"COMPUTER CHOSE: {input1}")
print(f"YOU CHOSE: {input2}")

if a==None:
    print("TIE, play again")
elif a==True:
    print("You win")
elif a==False:
    print("You Lose! Better Luck Next Time")
else :
    print("Wrong input play again")



