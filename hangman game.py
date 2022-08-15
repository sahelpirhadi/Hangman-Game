import random
from re import A
listofwords=["monghazi"]
guessright=[]
guesswrong=[]
myword=random.choice(listofwords)
pos_list = ['_' for x in range(len(myword))]
i=0
while i<6:
    s=True
    while s==True:
        if myword==("".join(pos_list)):
            print("you did this!")
            i=10
            break
        guess=input("please enter your guess: ")
        while ord(guess)<97 or ord(guess)>122:
            guess=input("please enter your guess in lower case: ")
        if (guess in guessright) or (guess in guesswrong):
            print("you guess it once please try again!")
        elif guess in myword:
            for j in [x for x, v in enumerate(myword) if v == guess]:
                pos_list[j]=guess
            guessright.append(guess)
            print("you guess right!")
            print("".join(pos_list))
        else:
            i=i+1
            guesswrong.append(guess)
            print("".join(pos_list))
            print(guesswrong)
            print(6-i,"chanses left!")
            s=False
            
if i!=10:
    print("you lose!")

