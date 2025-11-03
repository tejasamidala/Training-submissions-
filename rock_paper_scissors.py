import random

CHOICES = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(CHOICES)

def decide_winner(player, computer):
    if player == computer:
        return "tie"
    wins_over = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    return "player" if wins_over[player] == computer else "computer"

def play():
    print("🎮 Rock–Paper–Scissors (best of 5). Type q to quit.")
    player_score = 0
    computer_score = 0
    round_num = 1

    while player_score < 3 and computer_score < 3:
        choice = input(f"Round {round_num} — pick rock/paper/scissors: ").strip().lower()
        if choice == "q":
            print("Bye! 👋")
            return
        if choice not in CHOICES:
            print("Invalid choice. Try again.")
            continue

        comp = get_computer_choice()
        result = decide_winner(choice, comp)
        print(f"  You: {choice} | Computer: {comp}")

        if result == "player":
            player_score += 1
            print(f"  ✅ You win the round! Score {player_score}-{computer_score}\n")
        elif result == "computer":
            computer_score += 1
            print(f"  ❌ Computer wins the round! Score {player_score}-{computer_score}\n")
        else:
            print(f"  🤝 Tie. Score {player_score}-{computer_score}\n")

        round_num += 1

    print("🏁 Match over!")
    if player_score > computer_score:
        print("🎉 You win the match!")
    else:
        print("💻 Computer wins the match.")

play()