class CardGame:
    def __init__(self, player1_cards, player2_cards):
        self.player1 = list(player1_cards)
        self.player2 = list(player2_cards)
        self.max_rounds = 10 ** 6

