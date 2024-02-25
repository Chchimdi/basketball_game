import random


def regularball(score_array):
    currentscore = 0
    for i in range(5):
        if i == 4:
            if random.randint(0,1) == 1:
                currentscore += 2
                score_array.append("M")
            else:
                score_array.append("X")
        elif random.randint(0,1) == 1:
            score_array.append("O")
            currentscore += 1
        else:
            score_array.append("X")
    
    return currentscore, score_array

def moneyball(score_array):
    currentscore = 0
    for i in range(5):
        if random.randint(0,1) == 1:
            currentscore += 2
            score_array.append("M")
        else:
            score_array.append("X")

    return currentscore, score_array
    
def racks(moneyselect):
    playerscore = 0
    for i in range(1,6):
        score_array = []
        if i == moneyselect:
            results = moneyball(score_array)
            playerscore += results[0]
        else:
            results = regularball(score_array)
            playerscore += results[0]
        print(f"Rack {i} Score: {results[0]} | {results[1]}")
    print(f"Gsme Score: {playerscore}")

    return playerscore

def checkerror():
    while True:
        try:
            userinput = input('Enter value: ')
            userinput = int(userinput)
            if 1 <= userinput <= 5:
                break
            else:
                print("Enter a number from 1-5.")
        except ValueError:
            print('Enter a number.')
    
    return userinput

def run():
    moneyrack = checkerror()
    return racks(moneyrack)

def playagain():
    user_response = input("\nDo you want to play again? Y or N: ")
    while True:
        if user_response.lower() == "n":
            return False
        elif user_response.lower() == "y":
            return True
        else:
            user_response = input("Enter Y (yes) or N (No): ")
            continue

def main():
    player1score = player2score = gamesplayed = 0
    while True:
        print(f"Player 1's turn.")
        player1score += run()
        print(f"\nPlayer 2's turn.")
        player2score += run()
        gamesplayed += 1
        if not playagain():
            break
    print(f"Player1 score: {player1score}")
    print(f"Player2 score: {player2score}")
    print(f"Total potential points each: {34*gamesplayed}\n")
    
    print("Thanks for playing.")       

main()
   