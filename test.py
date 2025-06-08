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

    def play(self):
        rounds = 0
        while self.player1 and self.player2 and rounds < self.max_rounds:
            c1 = self.player1.pop(0)
            c2 = self.player2.pop(0)

            winner = self.compare_cards(c1, c2)
            if winner == 1:
                self.player1.extend([c1, c2])
            else:
                self.player2.extend([c1, c2])
            rounds += 1

        if rounds >= self.max_rounds:
            return "botva"
        elif not self.player2:
            return f"first {rounds}"
        else:
            return f"second {rounds}"

def read_cards(prompt):
    while True:
        try:
            input_str = input(prompt)
            cards = list(map(int, input_str.strip().split()))
            if len(cards) != 5 or any(c < 0 or c > 9 for c in cards):
                raise ValueError
            if len(set(cards)) != len(cards):
                raise ValueError("Карты не должны повторяться.")
            return cards
        except ValueError:
            print("Ошибка ввода! Введите 5 различных чисел от 0 до 9 через пробел.")

def main():
    print("Игра в пьяницу.")
    print("Введите 5 различных карт от 0 до 9 для каждого игрока (всего 10 карт, без повторов).")
    p1 = read_cards("Карты первого игрока: ")
    p2 = read_cards("Карты второго игрока: ")

    all_cards = set(p1 + p2)
    if len(all_cards) != 10:
        print("Ошибка: в игре должно быть 10 различных карт от 0 до 9.")
        return

    game = CardGame(p1, p2)
    result = game.play()
    print(result)


if __name__ == "__main__":
    main()
