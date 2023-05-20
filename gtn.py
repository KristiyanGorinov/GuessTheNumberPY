import random

easy = False
medium = False
hard = False


difficulty = (input("Choose difficulty: Press [e] for easy, Press [m] for medium, Press [h] for hard:   "))
if difficulty == 'e':
    easy = True
elif difficulty == 'm':
    medium = True
elif difficulty == 'h':
    hard = True
else:
    raise SystemExit("Invalid input, Please try again...")

if easy:
    computernumber = random.randint(1, 10)
    while True:
        player_number = int(input("Enter a number 1 to 10:   "))
        if player_number == computernumber:
            print("Congratulations, you won!!!")
            break
        elif player_number > computernumber:
            if player_number-computernumber > 5:
                print("Too High!!!")
                continue
            elif player_number-computernumber >= 1:
                print("Try a bit lower")
                continue
        elif player_number < computernumber:
            if computernumber-player_number > 5:
                print("Too Low!!!")
                continue
            elif computernumber-player_number >= 1:
                print("Try a bit higher")
                continue
if medium:
    computernumber = random.randint(1, 50)
    while True:
        player_number = int(input("Enter a number 1 to 50:   "))
        if player_number == computernumber:
            print("Congratulations, you won!!!")
            break
        elif player_number > computernumber:
            if player_number-computernumber > 10:
                print("Too High!!!")
                continue
            elif player_number-computernumber >= 1:
                print("Try a bit lower")
                continue
        elif player_number < computernumber:
            if computernumber-player_number > 10:
                print("Too Low!!!")
            elif computernumber-player_number >= 1:
                print("Try a bit higher")
                continue
if hard:
    computernumber = random.randint(1, 100)
    while True:
        player_number = int(input("Enter a number 1 to 100:   "))
        if player_number == computernumber:
            print("Congratulations, you won!!!")
            break
        elif player_number > computernumber:
            if player_number-computernumber > 20:
                print("Too High!!!")
                continue
            elif player_number-computernumber >= 1:
                print("Try a bit lower")
                continue
        elif player_number < computernumber:
            if computernumber-player_number > 20:
                print("Too Low!!!")
                continue
            elif computernumber-player_number >= 1:
                print("Try a bit higher")
                continue
