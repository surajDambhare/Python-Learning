# Q4 Build a number guessing game — computer picks a random number, user keeps guessing until correct
import random;
randomNumber = random.randint(1, 100);
tries = 0;

while True:
    tries += 1;

    userGuess = int(input("Guess a number between 1 and 100 :"));
    if userGuess == randomNumber:
        print(f"congratulations you have won  in {tries} tries!")
        break;
    elif userGuess < randomNumber:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")