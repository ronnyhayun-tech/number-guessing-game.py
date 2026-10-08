import random

class Solution(object):
    def numberGuessingGame(self):
        """
        :type: None
        :rtype: None
        """
        # Ronny Hayun, AM.
        # So that it generates a random whole number between 1 and 10
        random_number = random.randint(1, 10)
        
        # Create an empty list to store all of the valid guesses
        past_guesses = []
        
        # For Extra Credit: Start the player with 5 tries
        tries_left = 5
        
        # Set up a variable to track if the player has won
        correct_answer_picked = False
        
        # Keep playing while player hasn't won and still has tries remaining
        while correct_answer_picked == False and tries_left > 0:
            
            # Display remaining tries to the player
            print("You have " + str(tries_left) + " tries remaining.")
            
            # Ask the user to enter a guess
            user_guess = int(input("Enter a number between 1 - 10: "))
            
            # Check if their guess is outside 1-10 OR if it was already guessed
            # Repeated or invalid/non-number guesses do NOT use up a try
            while user_guess < 1 or user_guess > 10 or user_guess in past_guesses:
                
                # Check range validation
                if user_guess < 1 or user_guess > 10:
                    print("")
                    print("Invalid input!")
                    user_guess = int(input("Please enter a number between 1 and 10: "))
                    
                # Check duplicate validation
                elif user_guess in past_guesses:
                    print("")
                    print("You already guessed " + str(user_guess) + "!")
                    print("Choose a different number.")
                    print("")
                    print("Previous guesses: " + str(past_guesses))
                    print("")
                    print("You still have " + str(tries_left) + " tries remaining.")
                    user_guess = int(input("Enter a number between 1 - 10: "))
                    
            # Add the new valid guess to list
            past_guesses.append(user_guess)
            
            # Compare the guess to the random number
            if user_guess == random_number:
                print("")
                print("You guessed correctly! The number was " + str(random_number) + ".")
                print("")
                print("Your guesses: " + str(past_guesses))
                correct_answer_picked = True
                
            elif user_guess > random_number:
                # Subtract 1 try for a valid incorrect guess
                tries_left = tries_left - 1
                print("")
                print("Try again! The random number is lower!")
                print("")
                print("Previous guesses: " + str(past_guesses))
                print("")
                
            else:
                # Subtract 1 try for a valid incorrect guess
                tries_left = tries_left - 1
                print("")
                print("Try again! The random number is higher!")
                print("")
                print("Previous guesses: " + str(past_guesses))
                print("")
                
        # If player runs out of tries without guessing correctly
        if tries_left == 0 and correct_answer_picked == False:
            print("You ran out of tries!")
            print("")
            print("Your guesses were: " + str(past_guesses))
            print("")
            print("The correct number was " + str(random_number) + ".")
            print("")
            print("Game over!")


# Run my game
game = Solution()
game.numberGuessingGame()