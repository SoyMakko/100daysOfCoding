import random 

OPTIONS = ["Rock", "Paper", "Scissors"]
user_points = pc_points = 0
winner = []

for i in range (3):

    user_option = int(input("What do you choose? 0: Rock, 1: Paper, 2: Scissors"))
    pc_option = random.randint(0,2)

    print(f"User: {OPTIONS[user_option]} | PC: {OPTIONS[pc_option]}") 

    if (user_option == 0 and pc_option == 2):
        winner.append("user")
    elif(user_option == 1 and pc_option == 0):
        winner.append("user")
    elif(user_option == 2 and pc_option == 1):
        winner.append("user")
    elif(user_option == pc_option):
        winner.append("Tie")      
    else:
        winner.append("PC")

for i in range (len(winner)):
    if winner[i] == "user":
        user_points += 1
    else:
        pc_points+=1

print("points: ", winner)

if user_points > pc_points:
    print("🏆 You win!")
elif user_points < pc_points:
    print("❌ You lose!")
else:
    print("🤝 It's a tie!")