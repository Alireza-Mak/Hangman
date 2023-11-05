import random
from hangman_words import word_list, letters
from hangman_art import creator, logo, stages
reset = False
while not reset:
  end_of_game = False
  chosen_word = random.choice(word_list)
  word_length = len(chosen_word)
  chanceToGuess = len(stages)
  userWord =[]
  for _ in range(len(chosen_word)):
    userWord.append('-')
  status ="wrong"

  print(f"{creator}")
  print(f"{logo}")
  #Testing code
  print(f'Pssst, the solution is [ {chosen_word} ].')


  while not end_of_game:
    userCharacter = input("Guess a letter: ").lower()
    correctletter = True
    if userCharacter not in letters:
      correctletter = False
    while len(userCharacter) >1 or not correctletter:
      print("--------------------------")
      userCharacter = input(f"You guessed {userCharacter},that's not a letter, please guess correct format: ").lower()
      correctletter = True
    print("--------------------------")

    for index in range(len(chosen_word)):
      letter = chosen_word[index]
      if userCharacter == userWord[index]:
        status = "repeat"
      elif letter == userCharacter:
        userWord[index] =letter
        status ="find"
        
    if ( status== "wrong"):
      chanceToGuess -= 1
      print(f"You guessed {userCharacter},that's not in the word.You lost a life. 😞\nThe remaining life: {chanceToGuess}")
      print(stages[chanceToGuess])
      print("".join(str(char) for char in userWord))
      print("--------------------------")
    elif status =="find":
      print(f"You guessed corect.good job! 😊")
      print("".join(str(char) for char in userWord))
      print("--------------------------")

      status = "wrong"
    else:
      print(f"You have already guessed {userCharacter}.")
      print("".join(str(char) for char in userWord))
      print("--------------------------")
      status = "wrong"

    if "-" not in userWord:
      print("You Win!")
      print("\nCreated by:")
      print(f"{creator}\n")
      end_of_game =True
      resetGame = input("Do you wnat to repeat? Yes or No \n").lower()
      while resetGame != "yes" and resetGame != "no":
        resetGame = input("Do you wnat to repeat? Yes or No \n").lower()
      if resetGame == "no":
        reset = True
    elif chanceToGuess == 0:
      print("You Lose.")
      print("\nCreated by:")
      print(f"{creator}\n")
      end_of_game =True
      resetGame = input("Do you wnat to repeat? Yes or No \n").lower()
      while resetGame != "yes" and resetGame != "no":
        resetGame = input("Do you wnat to repeat? Yes or No \n").lower()
      if resetGame == "no":
        reset = True
