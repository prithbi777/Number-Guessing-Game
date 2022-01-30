import random
print("\n\n\n       ############## Welcome To The Number Guessing Game #############\n\n")
decide = 1
while (decide == 1):
    range = random.randint(5, 50)
    random_number = random.randint(0, range)
    print(f"####### The Number Is Between [{0} - {range}] #######")
    game_over = False
    count1 = 0
    count2 = 0
    player1 = input("Enter player-1 name : ")
    player2 = input("Enter player-2 name : ")
    print(f"Choose who will guess first :\n1. {player1}\n2. {player2}")
    turn = int(input("Enter [1-2] : "))

    while not game_over:
        if turn == 1:
            entered_number = int(input(f"{player1} guess the number : "))
            turn = 2
            if entered_number == random_number:
                print(
                    f"{player1}!! Your guess is Correct and the number is "+str(entered_number))
                count1 += 1
                if (count1 == 1):
                    print(f"You have guessed the number {count1} time!")
                else:
                    print(f"You have guessed the number {count1} times!")
                game_over = True
            else:
                if entered_number > random_number:
                    print("Your guess is at high!")
                    count1 += 1
                else:
                    print("Your guess is at low!")
                    count1 += 1
        elif turn == 2:
            entered_number = int(input(f"{player2} guess the number : "))
            turn = 1
            if entered_number == random_number:
                print(
                    f"{player2}!! Your guess is Correct and the number is "+str(entered_number))
                count2 += 1
                if (count2 == 1):
                    print(f"You have guessed the number {count2} time!")
                else:
                    print(f"You have guessed the number {count2} times!")
                game_over = True
            else:
                if entered_number > random_number:
                    print("Your guess is at high!")
                    count2 += 1
                else:
                    print("Your guess is at low!")
                    count2 += 1
        else:
            print("Invalid Number!")
            turn = int(input("Please Enter Again [1-2] : "))

    print("\n\n\t1. Play Again\n\t2. Exit")
    decide = int(input("\tEnter choice [1-2] : "))
    while True:
        if decide == 1:
            game_over = False
            break
        elif decide == 2:
            break
        else:
            print("\tInvalid Number!")
            decide = int(input("\tPlease Enter Again [1-2] : "))
    print("\n\n")

print("\n\n\n\n              ############## See You Again #############\n\n")
