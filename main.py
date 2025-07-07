import random

computer = random.choice([-1,0,1])

print("Enter stone or paper or scissor")

user_input = input("Enter your choice: ")
yourDict = {
            "stone" : 1,
            "paper" : 0,
            "scissor" : -1 
}
comp_Dict = {
            1 : "stone",
            0 : "paper",
            -1 : "scissor"
}
num = yourDict[user_input]

print(f"You choose {user_input}\nComputer choose {comp_Dict[computer]}")

if(computer == num):
    print("It's a draw")
else:
    if(computer==1 and num==0):
        print("You won")
    elif(computer==1 and num==-1):
        print("You lose")
    elif(computer==-1 and num==1):
        print("You won")
    elif(computer==-1 and num==0):
        print("You lose")
    elif(computer==0 and num==-1):
        print("You won")
    elif(computer==0 and num==1):
        print("You lose")
    else:
        print("Invalid Input")