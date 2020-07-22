import re
import random
import time


#### RULE SETUP ####

# match condition rules
# the key string shouldn't be changing at all, so this method should be reliable
def match_cond_one():
    # number match, return true if the number of two cards match
    match = False
    if (top_card[:1] == previous_card[:1]):
        match = True
    return match

def match_cond_two():
    # suit match - return true if the suit of the cards match
    match = False
    if (top_card[-5:-1] == previous_card[-5:-1]):
        match = True
    return match

def match_cond_three():
    # both number and suit match - return true if the cards match exactly
    # could also be interpreted as rules 1 and 2 being applied at the same time rather than both true at the same time
    match = False
    if (top_card == previous_card):
        match = True
    return match

# checking for a match - use the match condition chosen via user input
def check_match():
    if (matching_condition == "1"):
        return match_cond_one()
    elif (matching_condition == "2"):
        return match_cond_two()
    else:
        return match_cond_three()

# checking for winner - whichever player has the most cards - currently calls player 1 the winner if there were never any matches and both players have 0 cards...
def check_win():
    if (player_cards["p1"] == player_cards["p2"]):
        print("\nIt's a draw!")
    else:
        winner = max(player_cards, key=player_cards.get)
        print ("\n"+winner+" is the winner!")
    print ("\nPlayer totals: "+str(player_cards))
    

#### GAME SETUP ####

print("""
        Welcome to Match!

Cards will be played one by one.
When two consecutive cards match based on a given condition, 'Match!' should be declared.

The player who declares 'Match!' the quickest takes all the cards in the pile.
Keep going until all cards in the deck have been played.

The winner is whoever has the most cards in their hand the end of the game.

You will be given a chance to choose the number of card packs to use and the matching condition to play.

Press enter to continue...
""")

press_enter = input()

    
# ask how many card packs should be used - if blank or doesn't contain just a positive integer, ask again
# compiling regex first makes it quicker to run but as this is a small program and the two while loops are only run once (with correct input) i don't feel it's necessary here
# also - currently no limit to the number of packs but for practicality this should be introduced at some point...
packs = ""
while (not(re.search("^[1-9]*$", packs)) or packs is ""):
    print("How many packs of cards should be used? ")
    packs = str(input())


# ask which of the three matching conditions should be used - will keep asking until 1, 2 or 3 given as input
# can't choose number 3 with only one pack of cards - checks this
matching_condition = ""

while not (re.search("[123]", matching_condition)):
    print('''\nWhich of the three matching conditions should be used?

    1. Match based on face value
    2. Match based on suit
    3. Match based on face value and suit

Please enter 1, 2, or 3.''')

    matching_condition = input()

    if (matching_condition is "3" and packs is "1"):
        print("\nCannot match on face value and suit using only one pack of cards, please choose again")
        matching_condition = ""


# creating a dictionary of each card in play and the number of each
# key = face value and suit, value = the number left in the deck
# could use key = face value, value = suit - but the dictionary would be much larger
# figured this method was better due to less memory being used, less repitition within the dictionary and use of all()
suits = ["spades", "diamonds", "hearts", "clubs"]

deck_in_play = {}
card_no = int(1)

for item in suits:
    # after a quick google search, python apparently doesn't have swich/case statements and it's commonplace to just use if else blocks
    while (card_no <= 13):
        if(card_no == 1):
            card = "ace"
        elif(card_no == 11):
            card = "jack"
        elif(card_no == 12):
            card = "queen"
        elif(card_no == 13):
            card = "king"
        else:
            card = card_no
        deck_in_play[str(card) + " " + str(item)] = int(packs)
        card_no += 1
    card_no = 1

#print(deck_in_play)
            
# creating a list of each card in play
#suits = ["spades", "diamonds", "hearts", "clubs"]

#deck_in_play = []
#card_no = int(1)
#pack_no = int(1)

#while (pack_no <= int(packs)):
#    for item in suits:
#        while (card_no <= 13):
#            if (card_no == 10):
#                number = "T"
#            elif (card_no == 11):
#                number = "J"
#            elif (card_no == 12):
#                number = "Q"
#            elif (card_no == 13):
#                number = "K"
#            else:
#                number = card_no
#            deck_in_play.append(str(number) + item)
#            card_no += 1
#        card_no = 1
#    pack_no += 1

# shuffle the deck
#print ("\nShuffling deck...")
#random.shuffle(deck_in_play)


#### GAME START ####

# track the number of cards left in play, the size of the pile to give to a player when a match occurs and how many cards each player has
#total_cards = len(deck_in_play)
top_card = ""
pile = 0
player_cards = {"p1": 0, "p2": 0}

# while there are still cards in the deck
# generate a random number that will determine the card to pick - pretending the deck has been shuffled
# if key's value is 0 try again
# if not then play that card and minus that key's value by 1
keys = list(deck_in_play)

while not (all(value == 0 for value in deck_in_play.values())):
    card_to_play = random.randint(0,len(keys)-1)
    key = keys[card_to_play]

    if(deck_in_play[key] != 0):
        previous_card = top_card
        top_card = key
        print(top_card)
        pile += 1
        deck_in_play[key] -= 1

        if(check_match()):
            player = "p"+str(random.randint(1,2))
            player_cards[player] += pile
            pile = 0
            print("\nMatch! - pile won by player "+player)
            print("Cards held by each player: "+str(player_cards)+"\n")
        
#print(deck_in_play)

# while there are still cards left in the deck, deal the top card to the pile and check for a match against the previous card. If found add the pile to a random player's total.
#while (total_cards > 0):
#    previous_card = top_card
#    top_card = deck_in_play.pop()
#    pile += 1
#    print(top_card)
    #time.sleep(0.1)
#    if (check_match()):
#        player = "p"+str(random.randint(1,2))
#        player_cards[player] += pile
#        pile = 0
#        print("\nMatch! - pile won by player "+player)
#        print("Cards held by each player: "+str(player_cards)+"\n")
#    total_cards = len(deck_in_play)

check_win()



