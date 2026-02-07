

print('''                   __.--'~~~~~`--.
         ..       __.    .-~               ~-.
         ((\     /   `}.~                     `.
          \\\  .{     }               /     \   \
      (\   \\~~       }              |       }   \
       \`.-~ -@~     }  ,-,.         |       )    \
       (___     ) _}  (    :        |    / /      `._
        `----._-~.     _\ \ |_       \   / /-.__     `._
               ~~----~~  \ \| ~~--~~~(  + /     ~-._    ~-._
                         /  /         \  \          ~--.,___~_-_.
                      __/  /          _\  )
                    .<___.'         .<___/    ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

choice1 = input("Left or right? ").lower()

if choice1 == "left":
    choice2 = input("Swim or wait? ").lower()

    if choice2 == "wait":
        choice3 = input("Which door? Red, Blue, or Yellow? ").lower()

        if choice3 == "yellow":
            print("You Win! 🏆")
        elif choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
