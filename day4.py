# import random 

# OPTIONS = ["Rock", "Paper", "Scissors"]
# user_points = pc_points = 0


# for round_num in range(3):
#     print(f"\nRound {round_num + 1}")

#     user_option = int(input("Choose: 0 Rock, 1 Paper, 2 Scissors: "))
#     pc_option = random.randint(0, 2)

#     print(f"User: {OPTIONS[user_option]} | PC: {OPTIONS[pc_option]}")

#     if user_option == pc_option:
#         print("Tie!")
#     elif (user_option - pc_option) % 3 == 1:
#         user_points += 1
#         print("User wins the round!")
#     else:
#         pc_points += 1
#         print("PC wins the round!")

# print("\nFinal Score")
# print(f"User: {user_points} | PC: {pc_points}")

# if user_points > pc_points:
#     print("🏆 You win!")
# elif user_points < pc_points:
#     print("❌ You lose!")
# else:
#     print("🤝 It's a tie!")

import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        # Game state
        self.options = ["Rock", "Paper", "Scissors"]
        self.user_points = 0
        self.pc_points = 0
        self.rounds = 0
        self.max_rounds = 3

        # UI
        self.label_title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20))
        self.label_title.pack(pady=10)

        self.label_score = tk.Label(root, text=self.get_score_text(), font=("Arial", 14))
        self.label_score.pack()

        self.label_result = tk.Label(root, text="", font=("Arial", 14))
        self.label_result.pack(pady=10)

        # Buttons
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack()

        for i, option in enumerate(self.options):
            btn = tk.Button(self.frame_buttons, text=option, width=10,
                            command=lambda i=i: self.play_round(i))
            btn.grid(row=0, column=i, padx=10)

    def get_score_text(self):
        return f"User: {self.user_points} | PC: {self.pc_points} | Round: {self.rounds}/{self.max_rounds}"

    def play_round(self, user_option):
        if self.rounds >= self.max_rounds:
            return

        pc_option = random.randint(0, 2)
        self.rounds += 1

        result_text = f"User: {self.options[user_option]} | PC: {self.options[pc_option]}\n"

        # Game logic
        if user_option == pc_option:
            result_text += "Tie!"
        elif (user_option - pc_option) % 3 == 1:
            self.user_points += 1
            result_text += "User wins this round!"
        else:
            self.pc_points += 1
            result_text += "PC wins this round!"

        self.label_result.config(text=result_text)
        self.label_score.config(text=self.get_score_text())

        if self.rounds == self.max_rounds:
            self.show_final_winner()

    def show_final_winner(self):
        if self.user_points > self.pc_points:
            final_text = "🏆 YOU WIN!"
        elif self.user_points < self.pc_points:
            final_text = "❌ YOU LOSE!"
        else:
            final_text = "🤝 IT'S A TIE!"

        self.label_result.config(text=self.label_result.cget("text") + "\n\n" + final_text)


# Run app
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
