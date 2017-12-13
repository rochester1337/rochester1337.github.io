#Python story
print("\033[1;30;45m purple \n")

def greeting():
    print ("Helo...")
    response=input('Do you want to play a game ? (YES/NO)')
    return response

def second_choice():
    print ("Great. you hear a knock on the door, and hear someone say let me in.")
    response=input('{YES} (open it? And let the stranger in.) or {NO} (dont open it.)')
    return response

def haters(): #end game
    print("stranger comes in and shoots you. You are now dead GAME OVER!")

def third():
    print ("You hear more knocking and then gun shots ran throw the door!!!")
    response=input('{YES} (run to the back door.) or {NO} (stay and look for some thing to fight back with.)')
    return response




x = greeting()
x=x.upper()
if x=="YES":
    y = second_choice()
    y=y.upper()
    if y=="NO":
        z = third()
    else:
        haters()

else:
    print('bye')

