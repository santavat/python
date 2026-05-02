import random

print("\n=== MATCHSTICK GAME ===")
print("Rules: take 1–3 matches. Whoever takes the last one loses.\n")
input("Press Enter to start the game...\n")

difficulty = input("Choose difficulty (easy/medium/hard): ")


def game_computer_player():
    print('Flipping a coin...')
    result = random.choice([0, 1])

    if result == 1:
        print('You start')
        main_loop(1)
    else:
        print('Computer starts')
        main_loop(0)


def main_loop(turn):
    matches = 15
    take = 0

    while matches > 1:
        print(f"{matches} matches remaining\n")

        if turn == 0:
            print('Computer’s turn')

            if difficulty == "easy":
                if matches >= 3:
                    take = random.choice([1, 2, 3])
                elif matches == 2:
                    take = random.choice([1, 2])
                else:
                    take = 1
            elif difficulty == "medium":
                if random.random() < 0.7:
                    # same as hard difficulty
                    if (matches == 1 or matches % 4 == 1):
                        take = 1
                    elif (matches % 4 == 0):
                        take = 3
                    else:
                        take = (matches % 4) - 1
                else:
                    # random move like easy
                    take = random.randint(1, min(3, matches))
            else:
                if (matches == 1 or matches % 4 == 1):
                    take = 1
                elif (matches % 4 == 0):
                    take = 3
                else:
                    take = (matches % 4) - 1

            print('Computer took', take, 'match(es).')

        elif turn == 1:
            print('Your turn, enter how many matches you want to take.')
            while True:
                take = input()

                if take.isdigit():
                    take = int(take)

                    if take in [1, 2, 3]:
                        break
                    else:
                        print('You can only take 1, 2, or 3 matches.')
                else:
                    print('You entered text. Enter a number 1, 2, or 3.')

        matches -= take
        print(f"{matches} matches remaining\n")

        if matches == 1:

            if turn == 0:
                print('Game over. The computer won.')
            else:
                print('Game over. You won, congratulations :)')

        if matches == 0:
            if turn == 0:
                print('Game over. You won, congratulations')

            else:
                print('Game over. The computer won.')

        if turn == 0:
            turn = 1
        else:
            turn = 0


game_computer_player()