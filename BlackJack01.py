#blackjack
Import Random
Deck = {Two = 2, Three = 3, Four = 4, Five = 5, Six = 6, Seven = 7, Eight = 8, Nine = 9, Ten = 10, Jack = 10, Queen = 10, King = 10, Ace = 11} 
#Ace has multiple values but that can be sorted out once the user is dealt an Ace
def start()
    intro = input("Wanna play Blackjack? ")
    print(intro)
    if intro = "Yes":
        deal()

    elif intro = "No":
        maybe = input('Are you sure about that?')
        print(maybe)
        start()
    else:
        print('Please Enter a valid "Yes" or "No" please')
        start()

start()




def deal():
    cardA = random.choice(Deck)
    if cardA = Ace:
        responseA = input('You got an ace! Aces can have a value of either 11 or 1. Your ace is currently at 11; do you want to change it? ')
        print(responseA)
        if responseA = "Yes":
            Ace = 1
    cardB = random.choice(Deck)
    if cardB = Ace:
        responseB = input('You got an ace! Aces can have a value of either 11 or 1. Your ace is currently at 11; do you want to change it? ')
        print(responseB)
        if responseB = "Yes":
            Ace = 1
    userTotal = cardA + cardB
    print("You have", userTotal)


    cardC = random.choice(Deck)
    cardD = random.choice(Deck)
    botTotal = cardC + cardD 
    option()

def option()   
    choice = input('Do you want another card or showdown? ')
    if choice = "card":
        dealx()
    elif choice = "showdown":
        showdown()
    else:
        print("Please put valid response")
        option()

def dealx():
    cardC = random.choice(Deck)
    userTotal = userTotal + cardC
    showdown()

def showdown():
    print("Your opponent has", botTotal)
    
    if userTotal = botTotal:
        return "It's a draw!"
    elif userTotal = 21:
        return "You've won!"
    elif userTotal >= 22:
        return "You've lost..."
    elif userTotal > botTotal:
        return "You've won!"
    else:
        return "You've lost..."



