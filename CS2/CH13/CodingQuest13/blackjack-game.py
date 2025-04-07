import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def calculate_hand_value(self):
        value = 0
        aces = 0
        for card in self.hand:
            if card.value in ['Jack', 'Queen', 'King']:
                value += 10
            elif card.value == 'Ace':
                value += 11
                aces += 1
            else:
                value += int(card.value)

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def show_hand(self, hide_first_card=False):
        if hide_first_card:
            print(f"{self.name}'s hand: [Hidden Card, {', '.join(str(card) for card in self.hand[1:])}]")
        else:
            print(f"{self.name}'s hand: {', '.join(str(card) for card in self.hand)}")


class Bank:
    def __init__(self, starting_balance):
        self.balance = starting_balance

    def place_bet(self):
        if self.balance > 0:
            self.balance -= 1
            print(f"Bet placed. Remaining balance: ${self.balance}")
            return True
        else:
            print("You are out of money! Game over.")
            return False

    def win_bet(self):
        self.balance += 2
        print(f"You won the bet! New balance: ${self.balance}")

    def get_balance(self):
        return self.balance


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player")
        self.dealer = Player("Dealer")
        self.bank = Bank(3)

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

    def player_turn(self):
        while True:
            print(f"Your hand value: {self.player.calculate_hand_value()}")
            if self.player.calculate_hand_value() > 21:
                print("You busted!")
                return False
            choice = input("Do you want to 'hit' or 'stand'? ").lower()
            if choice == 'hit':
                self.player.add_card(self.deck.deal())
                print("Updated hand:")
                self.player.show_hand()
            elif choice == 'stand':
                break
        return True

    def dealer_turn(self):
        while self.dealer.calculate_hand_value() < 17:
            self.dealer.add_card(self.deck.deal())

    def determine_winner(self):
        player_value = self.player.calculate_hand_value()
        dealer_value = self.dealer.calculate_hand_value()

        print("\nFinal Hands:")
        self.player.show_hand()
        print(f"Your hand value: {player_value}")
        self.dealer.show_hand()
        print(f"Dealer's hand value: {dealer_value}")

        if player_value > 21:
            print("Dealer wins! You busted.")
            return "dealer"
        elif dealer_value > 21 or player_value > dealer_value:
            print("You win!")
            return "player"
        elif player_value < dealer_value:
            print("Dealer wins!")
            return "dealer"
        else:
            print("It's a tie!")
            return "tie"

    def play(self):
        print("Welcome to Blackjack!")
        print(f"Your starting balance is: ${self.bank.get_balance()}")
        choice = input("Do you want to start the game? (yes or no): ").lower()
        if choice != 'yes':
            print("Goodbye! Come back soon.")
            return

        while self.bank.get_balance() > 0:
            print("\nStarting a new round...")
            self.player.hand = []
            self.dealer.hand = []
            self.deck = Deck()
            self.deck.shuffle()

            if not self.bank.place_bet():
                break

            self.deal_initial_cards()
            self.player.show_hand()
            self.dealer.show_hand(hide_first_card=True)

            if not self.player_turn():
                print("You busted!")
            else:
                self.dealer_turn()
                winner = self.determine_winner()
                if winner == "player":
                    self.bank.win_bet()

            choice = input("Do you want to 'cash out' or 'keep playing'? ").lower()
            if choice == 'cash out':
                print(f"You cashed out with ${self.bank.get_balance()}!")
                return

        print("Game over! You are out of money.")


if __name__ == "__main__":
    game = BlackjackGame()
    game.play()