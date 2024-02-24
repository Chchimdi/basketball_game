import random

def regularball(score_array):
    currentscore = 0
    for i in range(5):
        if i == 4:
            if random.randint(0,1) == 1:
                currentscore += 2
                score_array.append(2)
            else:
                score_array.append(0)
        elif random.randint(0,1) == 1:
            score_array.append(1)
            currentscore += 1
        else:
            score_array.append(0)
    
    return currentscore, score_array

def moneyball(score_array):
    currentscore = 0
    for i in range(5):
        if random.randint(0,1) == 1:
            currentscore += 2
            score_array.append(2)
        else:
            score_array.append(0)

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
        print(f"Rack {i}: {results[1]}")

    return playerscore


def moneycheckerror():
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


print(f"Player 1's turn.")
moneyrack = moneycheckerror()
print(f"Score: {racks(moneyrack)}")
