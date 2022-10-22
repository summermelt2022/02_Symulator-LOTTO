from random import randint


def user_pick():
    """
    User chose to pick 6 numbers. Check if numbers are OK. Sort them.
    :return: List of chosen numbers.
    """

    dict_list = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
    }
    pick = []
    for j in range(1, 7):
        comment = ""
        while True:
            pick_number = input(f'{comment}Pick {dict_list.get(j)} number out of 49: ')
            if not pick_number.isnumeric():
                comment = f"    It's not a number. Chose number between 1 and 49.\n"
            elif 0 >= int(pick_number) or int(pick_number) > 49:
                comment = f"    Number needs to be in between 1 and 49.\n"
            elif int(pick_number) in pick:
                comment = f"    You already chose this number! Chose different number between 1 and 49.\n"
            else:
                pick.append(int(pick_number))
                break
    return sorted(pick)


def computer_pick():
    """
    Computer chose randomly 6 numbers. Sort them.
    :return: List of chosen numbers.
    """
    pick = []
    for e in range(1, 7):
        while True:
            pick_number = randint(1, 49)
            if pick_number in pick:
                continue
            else:
                pick.append(pick_number)
                break
    return sorted(pick)


def win(u, c):
    """
Looking for hit numbers.
    :param u: User chosen numbers list.
    :param c: Computer randomly chosen numbers list.
    :return: List containing hit numbers.
    """
    win_list = []
    for i in range(6):
        if u[i] in c:
            win_list.append(u[i])
    return win_list


def lotto_game():
    """
Game
    :return: Winning numbers
    """
    user_numbers = user_pick()
    print(f'You chose: {user_numbers}')
    computer_numbers = computer_pick()
    print(f'Computer draw: {computer_numbers}')

    dict_draw = {
        0: "zero numbers",
        1: "one number",
        2: "two numbers",
        3: "three numbers",
        4: "four numbers",
        5: "five numbers",
        6: "six numbers",
    }
    return print(f'You hit {dict_draw[len(win(user_numbers, computer_numbers))]}.')


lotto_game()
