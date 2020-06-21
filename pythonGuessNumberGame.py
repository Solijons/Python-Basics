low = 0.0
high = 100
guess = (high + low) / 2.0

print("Please think of a number between 0 and 100!")
print("Is your secret number", str(guess), "?")
ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while ans != 'c':
  if ans == 'h':
    high = guess
    guess = (low + high) // 2
    print("Is your secret number", str(guess), "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
  elif ans == 'l':
    low = guess
    guess = (low + high) // 2
    print("Is your secret number", str(guess), "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
  else:
    print("Sorry, I did not understand your input.")
    print("Is your secret number", str(guess), "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print("Game over. Your secret number was:", + guess)
