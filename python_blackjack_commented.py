import os
import random

# Initialise the list of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

# Function to deal the players hand
def deal(deck):
    hand = []
    for i in range(2):
	    random.shuffle(deck)
	    card = deck.pop()
	    if card == 11:card = "J"
	    if card == 12:card = "Q"
	    if card == 13:card = "K"
	    if card == 14:card = "A"
	    hand.append(card)
    return hand

# Function to start a new game or stop.
# Returns back to game after resetting both players hands.
def play_again():
    again = raw_input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
	    dealer_hand = []
	    player_hand = []
	    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	    game()
    else:
	    print "Bye!"
	    exit()

# Function to calculate the total value of the cards in the hand
def total(hand):
    total = 0
    for card in hand:
	    if card == "J" or card == "Q" or card == "K":
	        total+= 10
	    elif card == "A":
	        if total >= 11: total+= 1
	    else: total+= 11
	    else:
	    total += card
    return total

# Function to add a card to the hand of either the player or the dealer
def hit(hand):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	return hand

# Function to clear the users console window
def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')
# Function to print the hands and their total value for the user
def print_results(dealer_hand, player_hand):
	clear()
	print "The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand))
	print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))

# Function to print whether the player or the dealer got a blackjack if either got a blackjack
def blackjack(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print "Congratulations! You got a Blackjack!\n"
		play_again()
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print "Sorry, you lose. The dealer got a blackjack.\n"
		play_again()

# Function to compare the scores between the player and the dealer
def score(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print "Congratulations! You got a Blackjack!\n"
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print "Sorry, you lose. The dealer got a blackjack.\n"
	elif total(player_hand) > 21:
		print_results(dealer_hand, player_hand)
		print "Sorry. You busted. You lose.\n"
	elif total(dealer_hand) > 21:
		print_results(dealer_hand, player_hand)			   
		print "Dealer busts. You win!\n"
	elif total(player_hand) < total(dealer_hand):
		print_results(dealer_hand, player_hand)
   		print "Sorry. Your score isn't higher than the dealer. You lose.\n"
	elif total(player_hand) > total(dealer_hand):
		print_results(dealer_hand, player_hand)			   
		print "Congratulations. Your score is higher than the dealer. You win\n"		

# Function that contains the main interactions of the game.
# The function gives the player the opportunity to input how they want to interact with the game,
# taking their input and running the appropriate code.
def game():
	choice = 0
	clear()
	print "WELCOME TO BLACKJACK!\n"
	dealer_hand = deal(deck)
	player_hand = deal(deck)
	while choice != "q":
		print "The dealer is showing a " + str(dealer_hand[0])
		print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))
		blackjack(dealer_hand, player_hand)
		choice = raw_input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
		clear()
		if choice == "h":
			hit(player_hand)
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "s":
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "q":
			print "Bye!"
			exit()

# Replaces calling a main function by calling game instead	
if __name__ == "__main__":
   game()

# Code from the following repository: https://gist.github.com/mjhea0/5680216
# Code by mjhea0, commented by me