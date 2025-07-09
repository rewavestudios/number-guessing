import random  # Import the random module to generate random numbers
import sys     # Import sys for exiting the program if needed

# Track the best (lowest) score across games
best_score = None

# Infinite loop to allow replaying the game
while True:
    try:
        # Ask for valid range inputs inside a loop
        while True:
            try:
                min_val = int(input("Enter the minimum number: "))
                max_val = int(input("Enter the maximum number: "))
                if min_val >= max_val:
                    print("❗ Minimum must be less than maximum. Try again.")
                    continue
                break  # Exit loop when valid input is given
            except ValueError:
                print("⚠️ Invalid input. Please enter whole numbers.")

        # Ask for number of attempts
        while True:
            try:
                max_attempts = int(input("Enter the number of attempts allowed: "))
                if max_attempts <= 0:
                    print("❗ Attempts must be greater than 0.")
                    continue
                break
            except ValueError:
                print("⚠️ Please enter a valid number.")

        number_to_guess = random.randint(min_val, max_val)
        attempts_left = max_attempts
        guess_count = 0

        print(f"\n🎯 I have selected a number between {min_val} and {max_val}.")
        print(f"💡 You have {max_attempts} attempts to guess it.\n")

        # Game loop for guessing
        while attempts_left > 0:
            try:
                guess = int(input(f"Attempt #{guess_count + 1}: Your guess: "))
                guess_count += 1
                attempts_left -= 1

                if guess < number_to_guess:
                    print("🔻 Too low!")
                elif guess > number_to_guess:
                    print("🔺 Too high!")
                else:
                    print(f"✅ Congratulations! You guessed the number in {guess_count} attempts.")

                    # Update best score if this is the lowest guess count so far
                    if best_score is None or guess_count < best_score:
                        best_score = guess_count
                        print("🏆 New best score!")

                    break  # Correct guess

            except ValueError:
                print("⚠️ Please enter a valid number.")

        else:
            # Ran out of attempts
            print(f"\n❌ Out of attempts! The number was {number_to_guess}.")

        # Show best score
        if best_score is not None:
            print(f"📈 Best score so far: {best_score} attempts.")

        # Ask if user wants to play again
        play_again = input("\n🔁 Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing! Goodbye.")
            break

    except Exception as e:
        print(f"❗ Unexpected error: {e}")
