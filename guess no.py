gss=18
n=1
while(n<10):
    print("Enter your guess: ")
    num=int(input())
    if(num==gss):
        print("YOU WON")
        if n==1:
            print("You took",n,"guess")
        else:
            print("You took",n,"guesses")
        break

    elif(num>gss):
        print("It is a bit more","You have",10-n,"guesses left")

    else:
        print("It is a bit less","You have",10-n,"guesses left")
    print(n)
    n=n+1

else:
    print("You Lost")