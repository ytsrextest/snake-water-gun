import random
listt = ['s', 'w', 'g']
chance = 10
no_of_chance = 0
computer_Point = 0
human_Point = 0
print("\t\tSnake Water Gun Game")

while no_of_chance < chance:
    choose = random.choice(listt)
    # print(choose)
    print(f"\t\t{chance - no_of_chance} is Left Out of {chance}")
    mplay = input("\nPress s - For Snake\nPress w - For Water\nPress g - Fro Gun\n-->>>")

    if mplay == choose:
        print("Game Tie, Both Get 0 Point\n")
    elif mplay == 's' and choose == "g":
        computer_Point = computer_Point + 1
        print("Computer got 1 Point\n")
        print(f"Computer choose {choose} & You Choose {mplay}")
        print(f"Computer Point is {computer_Point} & Your Point is  {human_Point}\n")

    elif mplay == 's' and choose == 'w':
        human_Point = human_Point + 1
        print("You got 1 point\n")
        print(f"Computer choose {choose} & You Choose {mplay}")
        print(f"Computer Point is {computer_Point} & Your Point is  {human_Point}\n")

    elif mplay == 'w' and choose == 's':
        computer_Point = computer_Point + 1
        print("Computer got 1 point\n")
        print(f"Computer choose {choose} & You Choose {mplay}")
        print(f"Computer Point is {computer_Point} & Your Point is  {human_Point}\n")

    elif mplay == 'w' and choose == 'g':
        human_Point = human_Point + 1
        print("You got 1 point\n")
        print(f"Computer choose {choose} & You Choose {mplay}")
        print(f"Computer Point is {computer_Point} & Your Point is  {human_Point}\n")

    elif mplay == 'g' and choose == 's':
        human_Point = human_Point + 1
        print("You got 1 point\n")
        print(f"Computer choose {choose} & You Choose {mplay}")
        print(f"Computer Point is {computer_Point} & Your Point is  {human_Point}\n")

    elif mplay == 'g' and choose == 'w':
        computer_Point = computer_Point + 1
        print("Computer got 1 point\n")
        print(f"Computer choose {choose} & You Choose {mplay}")
        print(f"Computer Point is {computer_Point} & Your Point is  {human_Point}\n")
    # You Can Use Else here instant of elif
    elif mplay is not 'g' or 's' or 'w':
        print(f"{mplay} is An Invalid Input ! Please Try Again.\n")
        continue

    no_of_chance = no_of_chance + 1
    # print(f"{chance - no_of_chance} is Left Out of {chance}\n")


print("Game Over\n")
if computer_Point > human_Point:
    print("Computer Win This Game!")
    print(f"Your Point is {human_Point} & Computer Point is {computer_Point}")
elif computer_Point < human_Point:
    print("You Win This Game!")
    print(f"Your Point is {human_Point} & Computer Point is {computer_Point}")
