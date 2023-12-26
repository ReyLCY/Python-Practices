print("xxxx: Hello,there! ")
ans1=input("you: ")

print("3333: I am system 3333. \nPlease let know more infromation about you.")
name=input("3333: First.what's your name?  ")
print("3333: Hi,"+ name +".Nice to meet you!")
age=input("3333: How old are you?  ")
if int(age)<=3:
    print("3333: wowwww~ No wonder you look so young.●▼●")
elif 20>=int(age)>3:
    print("3333: What?!! I'm only 3 years old! Σ(°Д°;")
else :
    print("3333:Oh... Oh...∑(✘Д✘๑ )")
    print("3333: U kind of scare me....")

print("3333: anyway..")
print("3333: Hey! Hey! I'm bored.... Let's play some game?")
ans2= input("please answer YES or NO: ")
if ans2.upper() =="YES":
    print("3333: YES!! THAT'S MY BEST FRIEND! COMEON~●▼●")
elif ans2.upper() =="NO":
    print("3333: What?!! \nUmm... \nokay... \nare u sure? \nI beg you'll regrat about it! \n plz...")
    print("\n")
    print("well.. you know what? I don't care! ̿̿ ̿̿ ̿̿ ̿'̿’\̵͇̿̿\з=( ͠° ͟ʖ ͡°)=ε/̵͇̿̿/‘̿̿ ̿ ̿ ̿ ̿ ̿ ")

else :
    print("3333:Oh... Oh...∑(✘Д✘๑ ) What are you talking about?")
    print("well.. whatever! ₍₍ ◝('ω'◝) ⁾⁾ ₍₍ (◟'ω')◟ ⁾⁾")
    

print("3333: Let's play a game to guess my secret number!(◉３◉) \nNow please guess your first number from 1~100!")
print("3333: you only have three chances.")

import random


while True:
    bomb = random.randint(1,100)
    hight=100
    low =1
    count=1
    while count<=3:
        try:
            num = input("round: "+str(count)+"\nnumber should between "+str(low)+"~ "+str(hight)+":>> ")
        except ValueError:
            print("3333:plz enter a valid number~")
            continue
        
        if int(num)==bomb:
            print("congratulation! you find the password!")
            break
        elif int(num)<bomb:
            low=num
        else:
            hight=num
        
        count+=1
    
    if count==4:
        print(f"3333: haha~ You lose~ The correct number was{bomb}.")
        print("Do you want to play again?")
        ans3= input("please answer YES or NO: ")
        
        while True:
            if ans3.upper() =="NO":
                print("3333: okay~bye!bye!")
                exit()
            elif ans3.upper() =="YES":
                print("3333: okay~LET'S PLAY AGAIN!")
                break
            else :
                ans3= input("please answer YES or NO: ")
    else:
        break
