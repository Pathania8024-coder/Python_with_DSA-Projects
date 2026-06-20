secret_number = 7


while True:
              ask_number = int(input("Guess secret number : "))
              if ask_number > secret_number:
                      print("Guess lower")
              elif ask_number < secret_number:
                      print('Guess Higher')
              else:
                      print('You guessed correct number')
                      break