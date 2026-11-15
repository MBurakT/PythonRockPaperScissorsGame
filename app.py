import random


def play() -> None:
    random_list = ["1", "2", "3"]
    user_wins = 0
    computer_wins = 0

    while True:
        user_input = input("Enter 1 for rock, 2 for paper, 3 for scissors\n")

        if user_input not in random_list:
            print("Enter a valid argument!\n")
            continue

        random.shuffle(random_list)
        random.shuffle(random_list)
        chosen = random.choice(random_list)

        match chosen:
            case "1":
                if user_input == "1":
                    print(f"Computer: {chosen} User: {user_input} Draw!")
                elif user_input == "2":
                    print(f"Computer: {chosen} User: {user_input} User wins!")
                    user_wins += 1
                else:
                    print(
                        f"Computer: {chosen} User: {user_input} Computer wins!")
                    computer_wins += 1
            case "2":
                if user_input == "1":
                    print(
                        f"Computer: {chosen} User: {user_input} Computer wins!")
                    computer_wins += 1
                elif user_input == "2":
                    print(f"Computer: {chosen} User: {user_input} Draw!")
                else:
                    print(f"Computer: {chosen} User: {user_input} User wins!")
                    user_wins += 1
            case "3":
                if user_input == "1":
                    print(
                        f"Computer: {chosen} User: {user_input} User wins!")
                    user_wins += 1
                elif user_input == "2":
                    print(
                        f"Computer: {chosen} User: {user_input} Computer wins!")
                    computer_wins += 1
                else:
                    print(f"Computer: {chosen} User: {user_input} Draw!")

        print(
            f"Computer Score: {computer_wins} User Score: {user_wins}\n".center(50))


play()
