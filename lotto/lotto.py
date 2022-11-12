import random

banner = """    ____                          __          ____   _____ _         
   / __ \____ _      _____  _____/ /_  ____ _/ / /  / ___/(_)___ ___ 
  / /_/ / __ \ | /| / / _ \/ ___/ __ \/ __ `/ / /   \__ \/ / __ `__ \\
 / ____/ /_/ / |/ |/ /  __/ /  / /_/ / /_/ / / /   ___/ / / / / / / /
/_/    \____/|__/|__/\___/_/  /_.___/\__,_/_/_/   /____/_/_/ /_/ /_/ 
"""
print(banner)
print("Each powerball ticket costs: $2\nThe Jackpot is: $1.586 Billion\nthe odds are: 1 in 29,201,338.\nGood Luck!")

# Let the player enter the first five numbers, 1 to 69:
while True: 
    print("\nEnter five different numbers from 1 to 69, with spaces between.\
            \n each number. Ex: 12 23 42 30 5")
    response = input('> ')

    # check that the player entered 5 numbers.
    numbers = response.split()
    if len(numbers) != 5:
        print("Please enter five numbers, separated by spaces.")
        continue

    # convert string to integers:
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print("Please enter numbers, like 27, 12, or 50")
        continue

    # Check that numbers are between 1 and 69
    for i in range(5):
        if not (1 <= numbers[i] <= 69):
            print("The numbers but all be between 1 and 69")
            continue
    
    # Check that numbers are unique and create a set to remove dupes
    if len(set(numbers)) != 5:
        print("You must enter five different numbers")
        continue

    break

# Let the player select the power ball, 1 to 26
while True:
    print("Enter the powerball number from 1 to 26")
    response = input('> ')

    # Convert strings to integers
    try: 
        powerball = int(response)
    except ValueError:
        print("Please enter a number, like 3, 12, or 15")
        continue

    # Check that the number is between 1 and 26
    if not (1 <= powerball <= 26):
        print('The powerball number must be between 1 and 26.')
        continue

    break

# Enter number of times you want to play
while True:
    print("How many times do you want to play? (Max 1000000)")
    response = input('> ')

    # Convert strings to int
    try:
        numPlays = int(response)
    except ValueError:
        print('Please enter a number, like 12, 99, or 280000')
        continue

    #check that number is between 1 and 1000000
    if not (1 <= numPlays <= 1000000):
        print("You can play between 1 and 1000000 times.")
        continue
    break

# Run the simulation
playCounter = 0
price = '$' + str(2 * numPlays)
print(f"It costs {price} to play {numPlays} times but dont worry...\nI am sure you will win it all back!")
input("Press enter to start...")

possibleNUmbers = list(range(1, 70))
for i in range(numPlays):
    #come up with lottery numbers
    random.shuffle(possibleNUmbers)
    winningNumbers = possibleNUmbers[0:5]
    winningPowerball = random.randint(1, 26)

    #display winning numbers:
    print(f"The winning numbers are: {winningNumbers}\nThe powerball is: {winningPowerball}")

    if(set(numbers) == set(winningNumbers) and powerball == winningPowerball):
        print("\nYou have won the Poweball Lottery! Congradulations\n You would be a billionair if this were real!")
        break
    else:
        playCounter += 1
        print("You lost....")

timeNeededToWin = round(playCounter / 360)
print("\n\n=======================")
print(f"Final Assesment:\n\nYou played: {playCounter} times\nPlaying one ticket a day\nIt would take {timeNeededToWin} years to win\nAssuming you did not reach 1 million plays.\nYou have wasted: {price}\nThanks for playing!")
print("=======================")    

