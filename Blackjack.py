import random

import tkinter

# Function to take in the card Images
def load_images(card_images):
    suits=['club','diamond','heart','spade']
    face_cards=['jack','king','queen']
    extension='png'

    # For each suit, retrieve the card images
    for suit in suits:
        for card in range(1,11):
            name='F:\Programming\Python\Classwork-Modules and functions/cards/{}_{}.{}'.format(str(card),suit,extension)
            image=tkinter.PhotoImage(file=name)
            card_images.append((card,image,))

        # Now for the face cards
        for card in face_cards:
            name='F:\Programming\Python\Classwork-Modules and functions/cards/{}_{}.{}'.format(str(card),suit,extension)
            image=tkinter.PhotoImage(file=name)
            card_images.append((10,image,))


def score_hand(hand):
    #Calculate the total score of all the cards in the list.
    #Only one ace can have the value of 11, and this would reduce to 11 if the hand would bust.
    score=0
    ace=False
    for next_card in hand:
        card_value=next_card[0]
        if card_value==1 and not ace:
            ace=True
            card_value=11
        score += card_value
        #If we would bust, check if there is an ace and subtract 10
        if score>21 and ace:
            score -= 10
            ace=False
    return score


def deal_card(frame):
    # Pop the next card out of the deck
    next_card=deck.pop(0)
    #add it to the back of the deck
    deck.append(next_card)
    # Add the image to a label and display it
    tkinter.Label(frame,image=next_card[1],relief='raised').pack(side='left')
    # now return the cards face value
    return next_card


def deal_dealer():
    dealer_score=score_hand(dealer_hand)
    while 0< dealer_score<17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score=score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score=score_hand(player_hand)
    if player_score>21:
        result_text.set('Dealer Wins')
    elif dealer_score>21 or dealer_score<player_score:
        result_text.set('Player Wins')
    elif dealer_score>player_score:
        result_text.set('Dealer Wins')
    else:
        result_text.set('Draw')
    

def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score=score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score>21:
        result_text.set('Dealer Wins')
    # global player_score
    # global player_ace
    # card_value=deal_card(player_card_frame)[0]
    # if card_value==1 and not player_ace:
    #     card_value=11
    # player_score += card_value
    # # If we would bust, check if there is an ace and subtract it
    # if player_score<21 and player_ace:
    #     player_score-=10
    #     player_ace=False
    # player_score_label.set(player_score)
    # if player_score>21:
    #     result_text.set('Dealer Wins')


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # Embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame=tkinter.Frame(card_frame,background='black')
    dealer_card_frame.grid(row=0,column=1,sticky='ew',rowspan=2)
    #Embedded frame to hold the card images
    player_card_frame.destroy()
    player_card_frame=tkinter.Frame(card_frame,relief='sunken',background='green')
    player_card_frame.grid(row=2,column=1,rowspan=2,sticky='ew')

    result_text=''
    # Create a list to store the dealer's and player's cards
    player_hand=[]
    dealer_hand=[]

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def shuffle():
    random.shuffle(deck)
    

mainWindow=tkinter.Tk()
# Now setting up the frame for the dealer and the player

mainWindow.title("BlackJack")
mainWindow.geometry('640x480')
mainWindow.configure(background='green')

result_text=tkinter.StringVar()
result=tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0,column=0,columnspan=3)

card_frame=tkinter.Frame(mainWindow, relief='sunken',background='green',borderwidth='1')
card_frame.grid(row=1,column=0,sticky='ew',columnspan=3,rowspan=3)

dealer_score_label=tkinter.IntVar()
tkinter.Label(card_frame,text='Dealer',background='green',fg='white').grid(row=0,column=0)
tkinter.Label(card_frame,textvariable=dealer_score_label,background='green',fg='white').grid(row=1,column=0)

# embedded frame to hold the cards
dealer_card_frame=tkinter.Frame(card_frame,relief='sunken',background='green')
dealer_card_frame.grid(row=0,column=1,rowspan=2,sticky='ew')

player_score_label=tkinter.IntVar()
# player_score=0
# player_ace=False
tkinter.Label(card_frame,text="Player",background='green',fg='white').grid(row=2,column=0)
tkinter.Label(card_frame,textvariable=player_score_label,background='green',fg='white').grid(row=3,column=0)

# Embedded frame to hold the card images
player_card_frame=tkinter.Frame(card_frame,relief='sunken',background='green')
player_card_frame.grid(row=2,column=1,rowspan=2,sticky='ew')

button_frame=tkinter.Frame(mainWindow)
button_frame.grid(row=5,column=1,columnspan=3,sticky='w')

dealer_button=tkinter.Button(button_frame,text='Dealer',command=deal_dealer)
dealer_button.grid(row=0,column=0)

player_button=tkinter.Button(button_frame,text='Player',command=deal_player)
player_button.grid(row=0,column=1)

new_button=tkinter.Button(button_frame,text='New Game',command=new_game)
new_button.grid(row=0,column=2)

shuffle_button=tkinter.Button(button_frame,text='Shuffle',command=shuffle)
shuffle_button.grid(row=0,column=3)

cards=[]
load_images(cards)


# Create a deck of cards and shuffle them
deck=list(cards)
shuffle()

# Create a list to store the dealer's and player's cards
player_hand=[]
dealer_hand=[]
new_game()

mainWindow.mainloop()