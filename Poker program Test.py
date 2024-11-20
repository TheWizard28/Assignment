import random

class Deck():
    
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size
    
    def deal(self):
    #when the deck runs out of cards (paramater passes into class - ex: 52 bc 52 cards in a deck)
    #we need to reshuffle the deck
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
    #adding  one to current_card  can't be 0 - there is no 0 in a deck of cards
            self.current_card += 1
        return self.card_list[self.current_card - 1]

def main():

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    my_deck = Deck(52)
    #creating dictionary to hold your hand of 5 cards
    poker_hand_dict = []

    print(f'Deal 1')
    #looping 5 times because it is 5 hand poker
    for i in range(5):
        my_deck = Deck(52)
        d = my_deck.deal()
        r = d % 13
        s = d // 13
        print(ranks[r], 'of', suits[s])
        
        #creating a dictionary to hold the value of the card
        poker_hand_dict.append({i: (f'{ranks[r]} of {suits[s]}')})


    #create a list to hold cards the user wants to discard
    replacement_dict = []
    removed_card = []

    print('Please replace 3 cards.')
    for i in range(1,4):
        poker_replace = int(input('Which card number (1-5) do you want to replace? '))             
        removed_card = poker_hand_dict.pop(poker_replace - i)
        replacement_dict.append(removed_card)
        r = d % 13
        s = d // 13        
    
    my_deck = Deck(52)
    #creating dictionary to hold your hand of 5 cards
    new_hand_dict = []

    print(f'New Hand')
    #looping 5 times because it is 5 hand poker
    for i in range(5):
        my_deck_new = Deck(52)
        d = my_deck_new.deal()
        r = d % 13
        s = d // 13
        print(ranks[r], 'of', suits[s])
        
        #creating a dictionary to hold the value of the card
        new_hand_dict.append({i: (f'{ranks[r]} of {suits[s]}')})
    
    poker_hand_dict.append(new_hand_dict)
      
        
main()
