def hangman(word):
    wrong = 0
    stages = ["",
              "_________",
              "|      | ",
              "|      | ",
              "|      o ",
              "|     /|/",
              "|     // ",
              "|        "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Gra w wisielca")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Odgadnij litere: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("Wygrałes!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Przegrałes! miales odgadnac: {}".format(word))


hangman("polska")