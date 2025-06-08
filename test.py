class CardGame:
    def __init__(self, player1_cards, player2_cards):
        self.player1 = list(player1_cards)
        self.player2 = list(player2_cards)
        self.max_rounds = 10 ** 6

    def compare_cards(self, c1, c2):
        """Сравнивает две карты с учетом правила '0 бьет 9'."""
        if c1 == 0 and c2 == 9:
            return 1
        elif c1 == 9 and c2 == 0:
            return 2
        elif c1 > c2:
            return 1
        else:
            return 2
