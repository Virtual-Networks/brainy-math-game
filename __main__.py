import random
import operator


def score(level):
  """ Calculates the score at the end of every game """
  points = 0
  for item in range(1, level):
    if level < 10:
      points += 10 * item
    else:
      points += 20 * item
  return points

def rng(level, max_int, max_float):
  """ Generates a random number between 1 and the maximum number possible """
  if level < 10:
    return random.randint(1, max_int)
  elif level >= 10:
    return round(random.uniform(1, max_float), 2)

if __name__ == "__main__":
    game = True
    print("Welcome to the math game!")
    dif_float = 0
    level = 1  # Start on level one

    # Every possible operation for each problem
    operators = {
        1: (operator.add, "+"),  # Sum
        2: (operator.sub, "-"),  # Substraction
        3: (operator.mul, "*"),  # Multiplication
        4: (operator.truediv, "/")  # Division
    }

    while game is True:
        max_float = 0
        max_int = 0
        # The maximum possible number increases for every level
        if level < 10:
          max_int = level * 10
        else:
          max_float = dif_float * 10

        # Chooses a random operator for each level
        op_key = random.choice(list(operators.keys())[:min(level, 4)])
        operation, symbol = operators[op_key]

        # Generates a random number between 1 and the maximum number possible
        num1 = rng(level, max_int, max_float)
        num2 = rng(level, max_int if symbol != "/" else max(1, max_int // 2), max_float)

        if symbol == "/" and level < 10: # If working with int, result is int
          num1 *= num2 # If you multiply each number, an int result is given.

        while num2 == 0 and symbol == "/":             # Avoids dividing by 0.
          num2 = rng(level, max_int, max_float)

        # Shows the mathematical problem to the user
        print(f"Level {level}: How much is {num1} {symbol} {num2}?")

        try:
            # Storages the user's answer in a variable
            answer = float(input("Your answer: "))

            # Verifies if the answer is correct
            rounded = round(operation(num1, num2), 2)
            if answer == rounded:
                print("Correct! Continue to the next level.\n")
                level += 1  # If answer is correct, advances to the next level.
                if level >= 10: # If level is >= 10, float values start.
                  dif_float += 1 # The difficulty of floats increases per lvl.
            else:
                lost = True
                # Ends the game if answer is correct
                print(f"Incorrect. The answer was {rounded}.")
                print(f"Your final score was {score(level)}")
                while lost is True:
                  answer = input("Do you want to play again? (Yes/No)\n")
                  if answer.lower() == "yes":
                      level = 1
                      break
                  elif answer.lower() == "no":
                    print("Thanks for playing!")
                    game = False
                    break
                  else:
                    print("That is not a valid answer.")
        except ValueError:
            # Error handling if user does not input a valid number.
            print("That's not a valid input. Try it again.\n")
