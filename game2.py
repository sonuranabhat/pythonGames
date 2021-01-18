#snake water gun
import random
def game(input1,input2):
    if input1==input2:
        return None
    elif input1=='r':
        if input2=='s':
            return False
        elif input2=='p':
            return True
        else:
            return "invalid"
    elif input1=='p':
        if input2=='s':
            return True
        elif input2=='r':
            return False
        else:
            return "invalid"
    elif input1=='s':
        if input2=='p':
            return False
        elif input2=='r':
            return True
        else:
            return "invalid"
    
print("Computer's Turn: rock(r) paper(p) or scissors(s)")
r=random.randint(1,3)
if r==1:
    input1="r"
elif r==2:
    input1="p"
else :
    input1="s"
print("PLayer's Turn: ")
input2=input("enter rock(r) paper(p) or scissors(s):")
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



