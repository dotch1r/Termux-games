import os
import time
import random
import json
import sys


SCORE_FILE = "termux_games_scores.json"

def play_again():
    while True:
        print(" " * 10 + "Play again? (y/n): ", end="")
        answer = input().strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print(" " * 10 + "Please enter y or n.")

def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, 'r') as f:
            data = json.load(f)
            if "rock_paper_scissors" not in data:
                data["rock_paper_scissors"] = {"wins": 0, "losses": 0, "draws": 0}
            return data
    return {
        "tic_tac_toe": {"wins": 0, "losses": 0, "draws": 0},
        "hangman": {"easy_wins": 0, "easy_losses": 0, "medium_wins": 0, "medium_losses": 0, "hard_wins": 0, "hard_losses": 0},
        "number_guessing": {"wins": 0, "losses": 0, "total_attempts": 0, "games_played": 0},
        "rock_paper_scissors": {"wins": 0, "losses": 0, "draws": 0}
    }

def save_scores(scores):
    with open(SCORE_FILE, 'w') as f:
        json.dump(scores, f, indent=4)

scores = load_scores()

def update_score(game, result, difficulty=None, attempts=None):
    global scores
    if game == "tic_tac_toe":
        if result == "win":
            scores["tic_tac_toe"]["wins"] += 1
        elif result == "loss":
            scores["tic_tac_toe"]["losses"] += 1
        elif result == "draw":
            scores["tic_tac_toe"]["draws"] += 1
    elif game == "hangman":
        key_win = f"{difficulty}_wins"
        key_loss = f"{difficulty}_losses"
        if result == "win":
            scores["hangman"][key_win] += 1
        else:
            scores["hangman"][key_loss] += 1
    elif game == "number_guessing":
        scores["number_guessing"]["games_played"] += 1
        if result == "win":
            scores["number_guessing"]["wins"] += 1
        else:
            scores["number_guessing"]["losses"] += 1
        if attempts is not None:
            scores["number_guessing"]["total_attempts"] += attempts
    elif game == "rock_paper_scissors":
        if "rock_paper_scissors" not in scores:
            scores["rock_paper_scissors"] = {"wins": 0, "losses": 0, "draws": 0}
        if result == "win":
            scores["rock_paper_scissors"]["wins"] += 1
        elif result == "loss":
            scores["rock_paper_scissors"]["losses"] += 1
        elif result == "draw":
            scores["rock_paper_scissors"]["draws"] += 1
    save_scores(scores)

def animated_print(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animated_title():
    os.system('clear')
    
    title_lines = [
        "████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗    ",
        "╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝    ",
        "   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝     ",
        "   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗     ",
        "   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗    ",
        "   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ",
        "                                                          ",
        " ██████╗  █████╗ ███╗   ███╗███████╗███████╗             ",
        "██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝             ",
        "██║  ███╗███████║██╔████╔██║█████╗  ███████╗             ",
        "██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║             ",
        "╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║             ",
        " ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝             "
    ]
    
    print("\n")
    for line in title_lines:
        animated_print(line, delay=0.005)
    
    time.sleep(0.4)
    
    print("") 
    
    ascii_lines = [
        "░█▀▄░█░█░░░█▀▄░█▀█░▀█▀░█▀▀░█░█░░",
        "░█▀▄░░█░░░░█░█░█░█░░█░░█░░░█▀█░░",
        "░▀▀░░░▀░░░░▀▀░░▀▀▀░░▀░░▀▀▀░▀░▀░░"
    ]
    for line in ascii_lines:
        animated_print(" " * 5 + line, delay=0.005)
    
    time.sleep(0.3)
    
    welcome = "Welcome to Termux Games!"
    for _ in range(2):
        sys.stdout.write("\r" + " " * 10 + welcome + "   ")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + " " * 10 + " " * len(welcome) + "   ")
        sys.stdout.flush()
        time.sleep(0.15)
    print("\n" + " " * 10 + welcome + "\n")

def simple_title():
    os.system('clear')
    
    title_lines = [
        "████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗    ",
        "╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝    ",
        "   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝     ",
        "   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗     ",
        "   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗    ",
        "   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ",
        "                                                          ",
        " ██████╗  █████╗ ███╗   ███╗███████╗███████╗             ",
        "██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝             ",
        "██║  ███╗███████║██╔████╔██║█████╗  ███████╗             ",
        "██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║             ",
        "╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║             ",
        " ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝             "
    ]
    
    print("\n")
    for line in title_lines:
        print(line)
    
    print("")
    print("")
    
    ascii_lines = [
        " " * 5 + "░█▀▄░█░█░░░█▀▄░█▀█░▀█▀░█▀▀░█░█░░",
        " " * 5 + "░█▀▄░░█░░░░█░█░█░█░░█░░█░░░█▀█░░",
        " " * 5 + "░▀▀░░░▀░░░░▀▀░░▀▀▀░░▀░░▀▀▀░▀░▀░░"
    ]
    for line in ascii_lines:
        print(line)
    
    print("\n" + " " * 10 + "Welcome to Termux Games!\n")

def print_menu():
    print("[1] Tic-Tac-Toe")
    print("[2] Pong              (Coming Soon)")
    print("[3] Hangman")
    print("[4] Number Guessing")
    print("[5] Rock Paper Scissors")
    print("[6] Statistics")
    print("[7] Info")
    print("[8] Exit\n")

def show_coming_soon():
    os.system('clear')
    print("\n" * 5)
    print(" " * 18 + "COMING SOON")
    print("\n" * 5)
    time.sleep(2)
    os.system('clear')
    simple_title()  

def show_info():
    os.system('clear')
    print("\n" * 4)
    print(" " * 5 + "+" + "-" * 35 + "+")
    print(" " * 5 + "| Thank you for using TERMUX GAMES. |")
    print(" " * 5 + "+" + "-" * 35 + "+")
    print("\n" + " " * 5 + "DEVELOPERS: by dotch")
    print(" " * 17 + "by gimmikookie")
    print(" " * 5 + "TikTok: _dotch")
    print(" " * 5 + "TikTok: gimmikookie")
    print("\n" * 2)
    print(" " * 5 + "Press ENTER to exit.")
    
    input()
    os.system('clear')
    simple_title()  

def show_statistics():
    os.system('clear')
    print("\n" * 3)
    print(" " * 20 + "STATISTICS")
    print(" " * 15 + "========================")
    
    ttt = scores["tic_tac_toe"]
    total_ttt = ttt["wins"] + ttt["losses"] + ttt["draws"]
    win_rate_ttt = (ttt["wins"] / total_ttt * 100) if total_ttt > 0 else 0
    
    hng = scores["hangman"]
    total_hng_wins = hng["easy_wins"] + hng["medium_wins"] + hng["hard_wins"]
    total_hng_losses = hng["easy_losses"] + hng["medium_losses"] + hng["hard_losses"]
    total_hng = total_hng_wins + total_hng_losses
    win_rate_hng = (total_hng_wins / total_hng * 100) if total_hng > 0 else 0
    
    ng = scores["number_guessing"]
    total_ng = ng["wins"] + ng["losses"]
    win_rate_ng = (ng["wins"] / total_ng * 100) if total_ng > 0 else 0
    avg_attempts = ng["total_attempts"] / ng["games_played"] if ng["games_played"] > 0 else 0
    
    rps = scores.get("rock_paper_scissors", {"wins": 0, "losses": 0, "draws": 0})
    total_rps = rps["wins"] + rps["losses"] + rps["draws"]
    win_rate_rps = (rps["wins"] / total_rps * 100) if total_rps > 0 else 0
    
    total_games = total_ttt + total_hng + ng["games_played"] + total_rps
    
    print(" " * 8 + f"Total Games Played: {total_games}")
    print(" " * 8 + "========================\n")
    
    print(" " * 5 + "Tic-Tac-Toe:")
    print(" " * 8 + f"Wins: {ttt['wins']} | Losses: {ttt['losses']} | Draws: {ttt['draws']}")
    print(" " * 8 + f"Win Rate: {win_rate_ttt:.1f}%")
    print("")
    
    print(" " * 5 + "Hangman:")
    print(" " * 8 + f"Easy   : Wins {hng['easy_wins']} / Losses {hng['easy_losses']}")
    print(" " * 8 + f"Medium : Wins {hng['medium_wins']} / Losses {hng['medium_losses']}")
    print(" " * 8 + f"Hard   : Wins {hng['hard_wins']} / Losses {hng['hard_losses']}")
    print(" " * 8 + f"Overall Win Rate: {win_rate_hng:.1f}%")
    print("")
    
    print(" " * 5 + "Number Guessing:")
    print(" " * 8 + f"Wins: {ng['wins']} | Losses: {ng['losses']}")
    print(" " * 8 + f"Win Rate: {win_rate_ng:.1f}%")
    print(" " * 8 + f"Average Attempts: {avg_attempts:.1f}")
    print("")
    
    print(" " * 5 + "Rock Paper Scissors:")
    print(" " * 8 + f"Wins: {rps['wins']} | Losses: {rps['losses']} | Draws: {rps['draws']}")
    print(" " * 8 + f"Win Rate: {win_rate_rps:.1f}%")
    print("")
    
    games_played = {
        "Tic-Tac-Toe": total_ttt,
        "Hangman": total_hng,
        "Number Guessing": ng["games_played"],
        "Rock Paper Scissors": total_rps
    }
    most_played = max(games_played, key=games_played.get)
    print(" " * 8 + f"Most Played Game: {most_played} ({games_played[most_played]} games)")
    
    print("\n" + " " * 10 + "Press ENTER to return.")
    input()
    os.system('clear')
    simple_title()  

def tic_tac_toe():
    while True:
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
            simple_title()  
            return
        
        is_vs_bot = (mode_choice == '2')
        difficulty = None

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

        board = [' ' for _ in range(9)]
        current_player = 'X'

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
                        simple_title()
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

        game_over = False
        while not game_over:
            clear_and_show_board()
            
            if current_player == 'X' or not is_vs_bot:
                pos = get_player_move()
                if pos is None:
                    game_over = True
                    break
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
                print("\n" + " " * 11 + winner)
                update_score("tic_tac_toe", "win" if current_player == 'X' else "loss")
                game_over = True
            elif is_draw():
                clear_and_show_board()
                print("\n" + " " * 13 + "IT'S A DRAW!")
                update_score("tic_tac_toe", "draw")
                game_over = True

            if game_over:
                if play_again():
                    continue
                else:
                    print(" " * 5 + "(Returning to main menu, please wait...)")
                    time.sleep(2)
                    os.system('clear')
                    simple_title()
                    return

            current_player = 'O' if current_player == 'X' else 'X'

def pong():
    show_coming_soon()

def hangman():
    while True:
        os.system('clear')
        print("\n" * 3)
        print(" " * 10 + "HANGMAN")
        print(" " * 8 + "Choose difficulty:\n")
        print("  [1] Easy")
        print("  [2] Medium")
        print("  [3] Hard")
        print("\n" + " " * 8 + "Select (1-3): ", end="")
        diff_choice = input().strip()

        if diff_choice not in ['1', '2', '3']:
            print("\n" + " " * 8 + "Invalid choice. Returning...")
            time.sleep(2)
            simple_title()
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
                simple_title()
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
            update_score("hangman", "win", difficulty.lower())
        else:
            print(" " * 10 + "😔 YOU LOSE! 😔")
            print(" " * 10 + f"The word was: {word}")
            update_score("hangman", "loss", difficulty.lower())

        if play_again():
            continue
        else:
            print(" " * 5 + "(Returning to main menu, please wait...)")
            time.sleep(2)
            os.system('clear')
            simple_title()
            return

def number_guessing():
    while True:
        os.system('clear')
        print("\n" * 3)
        print(" " * 10 + "NUMBER GUESSING")
        print(" " * 8 + "Guess the number between 1 and 100")
        print(" " * 8 + "You have 10 attempts!")
        print("\n" + " " * 8 + "Press ENTER to start...")
        input()

        secret_number = random.randint(1, 100)
        attempts_left = 10
        attempts_used = 0
        guessed = False

        while attempts_left > 0:
            os.system('clear')
            print(" " * 5 + "NUMBER GUESSING")
            print(" " * 5 + f"Attempts left: {attempts_left}")
            print(" " * 5 + "Guess a number (1-100 or 0 to quit): ", end="")

            try:
                guess = int(input().strip())
            except ValueError:
                print(" " * 5 + "Invalid! Enter a number.")
                time.sleep(1.2)
                continue

            attempts_used += 1

            if guess == 0:
                print(" " * 5 + "Game quit...")
                time.sleep(1.5)
                os.system('clear')
                simple_title()
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

            attempts_left -= 1
            time.sleep(1)

        os.system('clear')
        if guessed:
            print(" " * 10 + "🎉 YOU WIN! 🎉")
            print(" " * 10 + f"The number was: {secret_number}")
            update_score("number_guessing", "win", attempts=attempts_used)
        else:
            print(" " * 10 + "😔 YOU LOSE! 😔")
            print(" " * 10 + f"The number was: {secret_number}")
            update_score("number_guessing", "loss", attempts=attempts_used)

        if play_again():
            continue
        else:
            print(" " * 5 + "(Returning to main menu, please wait...)")
            time.sleep(2)
            os.system('clear')
            simple_title()
            return

def rock_paper_scissors():
    while True:
        os.system('clear')
        print("\n" * 3)
        print(" " * 5 + "ROCK PAPER SCISSORS 🔥")
        print("\n")
        print(" " * 8 + "Best of 5 - First to 3 wins")
        print("\n")
        print(" " * 8 + "Your choices:")
        print(" " * 10 + "r - Rock")
        print(" " * 10 + "p - Paper")
        print(" " * 10 + "s - Scissors")
        print(" " * 10 + "q - Quit")
        print("\n" * 2)
        print(" " * 8 + "Press ENTER to start...")
        input()

        player_score = 0
        computer_score = 0
        rounds = 0

        rock = "ROCK ✊"
        paper = "PAPER ✋"
        scissors = "SCISSORS ✌️"

        while player_score < 3 and computer_score < 3:
            os.system('clear')
            print("\n" * 2)
            print(" " * 5 + "ROCK PAPER SCISSORS 🔥")
            print(" " * 8 + f"Score: You {player_score}   Computer {computer_score}")
            print(" " * 8 + f"Round {rounds + 1}")
            print("\n")
            print(" " * 8 + "Your move (r / p / s / q): ", end="")

            player_choice = input().strip().lower()

            if player_choice == 'q':
                print(" " * 10 + "Game quit.")
                time.sleep(1.5)
                os.system('clear')
                simple_title()
                return

            if player_choice not in ['r', 'p', 's']:
                print(" " * 8 + "Invalid move! Use r, p or s.")
                time.sleep(1.2)
                continue

            computer_choice = random.choice(['r', 'p', 's'])

            rounds += 1
            os.system('clear')
            print("\n" * 2)
            print(" " * 8 + f"You chose: {rock if player_choice == 'r' else paper if player_choice == 'p' else scissors}")
            print(" " * 8 + f"Computer chose: {rock if computer_choice == 'r' else paper if computer_choice == 'p' else scissors}")
            print("\n")

            if player_choice == computer_choice:
                print(" " * 12 + "DRAW! 🤝")
                update_score("rock_paper_scissors", "draw")
            elif (player_choice == 'r' and computer_choice == 's') or \
                 (player_choice == 'p' and computer_choice == 'r') or \
                 (player_choice == 's' and computer_choice == 'p'):
                print(" " * 12 + "WIN! 🎉")
                player_score += 1
                update_score("rock_paper_scissors", "win")
            else:
                print(" " * 12 + "LOSS! 💀")
                computer_score += 1
                update_score("rock_paper_scissors", "loss")

            time.sleep(2.2)

        os.system('clear')
        print("\n" * 3)
        print(" " * 5 + "GAME OVER")
        print(" " * 8 + f"Final Score: You {player_score} - Computer {computer_score}")
        print("\n")
        if player_score == 3:
            print(" " * 8 + "YOU WIN THE GAME! 🎊🎉")
            print(" " * 8 + "Legendary performance king! 🔥")
        else:
            print(" " * 8 + "YOU LOSE THE GAME! 😔")
            print(" " * 8 + "One more try? You can crush it next time!")

        print("\n" * 2)
        if play_again():
            continue
        else:
            print(" " * 8 + "Returning to main menu...")
            time.sleep(2)
            os.system('clear')
            simple_title()
            return

def main():
    os.system('clear')
    animated_title()  

    while True:
        print_menu()
        choice = input("Your choice (1-8): ").strip().lower()

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
            rock_paper_scissors()
        elif choice == '6':
            show_statistics()
        elif choice == '7':
            show_info()
        elif choice == '8':
            print("Exiting Termux Games...")
            time.sleep(1)
            os.system('clear')
            break
        else:
            print("Invalid choice. Please try again...\n")
            time.sleep(1.2)
            simple_title()

if __name__ == "__main__":
    main()