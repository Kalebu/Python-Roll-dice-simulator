from random import randint 

while True:
    dice_random = randint(1, 6)
    print('Print Rolled dice ', dice_random)
    print('Should I generate again  ?')
    again = int(input('1.Yes\n2.No\n\nEnter option here : ')) 
    if again != 1:
        break
print('Thanks for playing the game')   