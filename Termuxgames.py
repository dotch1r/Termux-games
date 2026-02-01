import os
import time
import random

def print_title():
    title = '''
████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗    
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝    
   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝     
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗     
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗    
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝    
                                                         
 ██████╗  █████╗ ███╗   ███╗███████╗███████╗             
██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝             
██║  ███╗███████║██╔████╔██║█████╗  ███████╗             
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║             
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║             
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝             
    '''
    print(title)
    print(" " * 5 + "░█▀▄░█░█░░░█▀▄░█▀█░▀█▀░█▀▀░█░█░░")
    print(" " * 5 + "░█▀▄░░█░░░░█░█░█░█░░█░░█░░░█▀█░░")
    print(" " * 5 + "░▀▀░░░▀░░░░▀▀░░▀▀▀░░▀░░▀▀▀░▀░▀░░")
    print("\nWelcome to Termux Games!\n")

def print_menu():
    print("[1] Tic-Tac-Toe")
    print("[2] Pong              (Coming Soon)")
    print("[3] Hangman")
    print("[4] Number Guessing")
    print("[5] Info")
    print("[6] Exit\n")

def show_coming_soon():
    os.system('clear')
    print("\n" * 5)
    print(" " * 18 + "COMING SOON")
    print("\n" * 5)
    time.sleep(2)
    os.system('clear')
    print_title()

def show_info():
    os.system('clear')
    print("\n" * 4)
    print(" " * 5 + "+" + "-" * 35 + "+")
    print(" " * 5 + "| Thank you for using TERMUX GAMES. |")
    print(" " * 5 + "+" + "-" * 35 + "+")
    print("\n" + " " * 5 + "DEVELOPER: by dotch")
    print(" " * 5 + "           by gimmekookie")
    print(" " * 5 + "TikTok: _dotch")
    print(" " * 5 + "TikTok: gimmekookie")
    print("\n" * 2)
    print(" " * 5 + "Press ENTER to exit.")
    
    input()
    os.system('clear')
    print_title()

def tic_tac_toe():
    os.system('clear')
    print("\n" * 3)
    print(" " * 10 + "Tic-Tac-Toe\n")
    print("  [1] Player vs Player")
    print("  [2] Player vs Computer")
    print("\n" + " " * 8 + "Choose mode (1 or 2): ", end="")
    mode_choice = input().strip()
    
    if mode_choice not in ['1', '2']:
        print("\nInvalid choice. Returning to menu...")
        time.sleep(2)
        return
    
    is_vs_bot = (mode_choice == '2')
    board = [' ' for _ in range(9)]
    current_player = 'X'

    if is_vs_bot:
        os.system('clear')
        print("\n" * 3)
        print(" " * 8 + "Choose difficulty:\n")
        print("  [1] Easy")
        print("  [2] Medium")
        print("  [3] Hard")
        print("\n" + " " * 8 + "Select (1-3): ", end="")
        diff_choice = input().strip()
        difficulty = 'medium'
        if diff_choice == '1':
            difficulty = 'easy'
        elif diff_choice == '2':
            difficulty = 'medium'
        elif diff_choice == '3':
            difficulty = 'hard'
        print("\n" + " " * 8 + f"Difficulty: {difficulty.capitalize()}")
        time.sleep(1.5)
    else:
        difficulty = None

    def clear_and_show_board():
        os.system('clear')
        print("\n")
        print(" " * 10 + "Tic-Tac-Toe")
        print()
        print(" " * 9 + f" {board[0]} | {board[1]} | {board[2]} ")
        print(" " * 9 + "---+---+---")
        print(" " * 9 + f" {board[3]} | {board[4]} | {board[5]} ")
        print(" " * 9 + "---+---+---")
        print(" " * 9 + f" {board[6]} | {board[7]} | {board[8]} ")
        print("\n")
        if is_vs_bot:
            print(" " * 9 + f"{'Your turn (X)' if current_player == 'X' else 'Computer turn (O)'}")
        else:
            print(" " * 9 + f"Player {current_player}'s turn")
        print(" " * 9 + "Enter 1-9 or 0 to quit")

    def check_winner(player):
        wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        return any(all(board[i] == player for i in combo) for combo in wins)

    def is_draw():
        return ' ' not in board

    def get_player_move():
        while True:
            try:
                inp = input("\n" + " " * 9 + "Move (1-9 or 0 to quit): ").strip()
                if inp == '0':
                    print(" " * 9 + "Quitting game...")
                    time.sleep(1)
                    os.system('clear')
                    print_title()
                    return None
                pos = int(inp) - 1
                if 0 <= pos <= 8 and board[pos] == ' ':
                    return pos
                print(" " * 9 + "Invalid or taken!")
            except:
                print(" " * 9 + "Please enter a number!")

    def bot_move_easy():
        available = [i for i in range(9) if board[i] == ' ']
        return random.choice(available) if available else None

    def bot_move_medium():
        for p in ['O', 'X']:
            for i in range(9):
                if board[i] == ' ':
                    board[i] = p
                    if check_winner(p):
                        board[i] = ' '
                        return i
                    board[i] = ' '
        if board[4] == ' ':
            return 4
        corners = [0,2,6,8]
        random.shuffle(corners)
        for c in corners:
            if board[c] == ' ':
                return c
        edges = [1,3,5,7]
        random.shuffle(edges)
        for e in edges:
            if board[e] == ' ':
                return e
        return None

    def minimax(b, depth, is_max):
        if check_winner('O'): return 10 - depth
        if check_winner('X'): return depth - 10
        if is_draw(): return 0
        if is_max:
            best = -999
            for i in range(9):
                if b[i] == ' ':
                    b[i] = 'O'
                    best = max(best, minimax(b, depth+1, False))
                    b[i] = ' '
            return best
        else:
            best = 999
            for i in range(9):
                if b[i] == ' ':
                    b[i] = 'X'
                    best = min(best, minimax(b, depth+1, True))
                    b[i] = ' '
            return best

    def bot_move_hard():
        best_score = -999
        best_move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, 0, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    while True:
        clear_and_show_board()
        
        if current_player == 'X' or not is_vs_bot:
            pos = get_player_move()
            if pos is None:
                return
        else:
            print(" " * 9 + "Computer thinking...")
            time.sleep(0.6 if difficulty == 'easy' else 1.0)
            if difficulty == 'easy':
                pos = bot_move_easy()
            elif difficulty == 'medium':
                pos = bot_move_medium()
            else:
                pos = bot_move_hard()
            print(" " * 9 + f"Computer played → {pos+1}")

        board[pos] = current_player

        if check_winner(current_player):
            clear_and_show_board()
            winner = "You WIN!" if (is_vs_bot and current_player == 'X') else f"Player {current_player} WINS!" if not is_vs_bot else "Computer WINS!"
            print("\n" + " " * 11 + f"🎉 {winner} 🎉")
            time.sleep(3)
            os.system('clear')
            print_title()
            return

        if is_draw():
            clear_and_show_board()
            print("\n" + " " * 13 + "IT'S A DRAW!")
            time.sleep(3)
            os.system('clear')
            print_title()
            return

        current_player = 'O' if current_player == 'X' else 'X'

def pong():
    show_coming_soon()

def hangman():
    os.system('clear')
    print("\n" * 3)
    print(" " * 10 + "HANGMAN")
    print(" " * 8 + "Choose difficulty:\n")
    print(" " * 10 + "[1] Easy")
    print(" " * 10 + "[2] Medium")
    print(" " * 10 + "[3] Hard")
    print("\n" + " " * 8 + "Select (1-3): ", end="")
    diff_choice = input().strip()

    if diff_choice not in ['1', '2', '3']:
        print("\n" + " " * 8 + "Invalid choice. Returning...")
        time.sleep(2)
        return

    difficulty = 'Medium'
    if diff_choice == '1':
        difficulty = 'Easy'
    elif diff_choice == '2':
        difficulty = 'Medium'
    elif diff_choice == '3':
        difficulty = 'Hard'

    word_lists = {
        'Easy': [
            "cat", "dog", "bird", "fish", "tree", "sun", "moon", "star", "car", "house",
            "ball", "book", "door", "pen", "red", "blue", "green", "yellow", "apple", "banana",
            "cake", "milk", "bread", "egg", "hat", "shoe", "hand", "foot", "eye", "nose",
            "mouth", "ear", "arm", "leg", "baby", "boy", "girl", "man", "woman", "run",
            "jump", "eat", "drink", "sleep", "walk", "talk", "play", "read", "write", "smile"
        ],
        'Medium': [
            "python", "hangman", "computer", "keyboard", "terminal", "program", "developer",
            "flower", "garden", "mountain", "river", "school", "teacher", "coffee", "pizza",
            "football", "basketball", "soccer", "tennis", "guitar", "piano", "music", "island",
            "village", "window", "umbrella", "notebook", "planet", "queen", "ocean"
        ],
        'Hard': [
            "elephant", "kangaroo", "rhinoceros", "crocodile", "butterfly", "strawberry", "chocolate",
            "dictionary", "octopus", "penguin", "giraffe", "zebra", "hippopotamus", "alligator",
            "microphone", "television", "refrigerator", "automobile", "helicopter", "motorcycle",
            "university", "hospital", "restaurant", "beautiful", "dangerous", "mysterious", "adventure"
        ]
    }

    word_list = word_lists[difficulty]
    word = random.choice(word_list).upper()
    guessed = ['_'] * len(word)
    wrong_letters = []
    attempts = 6
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        GAME OVER!
        """
    ]

    os.system('clear')
    print("\n" * 2)
    print(" " * 8 + f"Difficulty: {difficulty}")
    print(" " * 8 + "Press ENTER to start...")
    input()

    while attempts > 0 and '_' in guessed:
        os.system('clear')
        print(" " * 5 + "HANGMAN - " + difficulty)
        print(stages[6 - attempts])
        print("\n" + " " * 5 + "Word: " + ' '.join(guessed))
        print(" " * 5 + "Wrong letters: " + ', '.join(wrong_letters))
        print(" " * 5 + f"Attempts left: {attempts}")
        print(" " * 5 + "Guess a letter (a-z or 0 to quit): ", end="")

        raw_input = input().strip()

        if raw_input == '0':
            print(" " * 5 + "Game quit...")
            time.sleep(1.5)
            os.system('clear')
            print_title()
            return

        guess = ''.join(c for c in raw_input.upper() if c.isalpha())

        if len(guess) != 1 or guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print(" " * 5 + "Invalid! Only English letters (a-z) allowed.")
            time.sleep(1.2)
            continue

        if guess in wrong_letters or guess in guessed:
            print(" " * 5 + "You already tried that letter!")
            time.sleep(1.2)
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print(" " * 5 + "Correct letter!")
        else:
            wrong_letters.append(guess)
            attempts -= 1
            print(" " * 5 + "Wrong letter!")

        time.sleep(1)

    os.system('clear')
    print(stages[6 - attempts])
    if '_' not in guessed:
        print(" " * 10 + "🎉 YOU WIN! 🎉")
        print(" " * 10 + f"The word was: {word}")
    else:
        print(" " * 10 + "YOU LOSE! 😔")
        print(" " * 10 + f"The word was: {word}")

    print("\n" * 2 + " " * 5 + "(Returning to main menu, please wait...)")
    time.sleep(4)
    os.system('clear')
    print_title()

def number_guessing():
    os.system('clear')
    print("\n" * 3)
    print(" " * 10 + "NUMBER GUESSING")
    print(" " * 8 + "Guess the number between 1 and 100")
    print(" " * 8 + "You have 10 attempts!")
    print("\n" + " " * 8 + "Press ENTER to start...")
    input()

    secret_number = random.randint(1, 100)
    attempts = 10
    guessed = False

    while attempts > 0:
        os.system('clear')
        print(" " * 5 + "NUMBER GUESSING")
        print(" " * 5 + f"Attempts left: {attempts}")
        print(" " * 5 + "Guess a number (1-100 or 0 to quit): ", end="")

        try:
            guess = int(input().strip())
        except ValueError:
            print(" " * 5 + "Invalid! Enter a number.")
            time.sleep(1.2)
            continue

        if guess == 0:
            print(" " * 5 + "Game quit...")
            time.sleep(1.5)
            os.system('clear')
            print_title()
            return

        if guess < 1 or guess > 100:
            print(" " * 5 + "Number must be between 1 and 100!")
            time.sleep(1.2)
            continue

        if guess == secret_number:
            guessed = True
            break
        elif guess < secret_number:
            print(" " * 5 + "Too low!")
        else:
            print(" " * 5 + "Too high!")

        attempts -= 1
        time.sleep(1)

    os.system('clear')
    if guessed:
        print(" " * 10 + "🎉 YOU WIN! 🎉")
        print(" " * 10 + f"The number was: {secret_number}")
    else:
        print(" " * 10 + "YOU LOSE! 😔")
        print(" " * 10 + f"The number was: {secret_number}")

    print("\n" * 2 + " " * 5 + "(Returning to main menu, please wait...)")
    time.sleep(4)
    os.system('clear')
    print_title()

def main():
    os.system('clear')
    print_title()

    while True:
        print_menu()
        choice = input("Your choice (1-6): ").strip().lower()

        os.system('clear')

        if choice == '1':
            tic_tac_toe()
        elif choice == '2':
            show_coming_soon()
        elif choice == '3':
            hangman()
        elif choice == '4':
            number_guessing()
        elif choice == '5':
            show_info()
        elif choice == '6':
            print("Exiting Termux Games...")
            time.sleep(1)
            os.system('clear')
            break
        else:
            print("Invalid choice. Please try again...\n")
            time.sleep(1.2)
            os.system('clear')
            print_title()

if __name__ == "__main__":
    main()
