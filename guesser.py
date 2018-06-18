from math import log, ceil


def check_valid_input(valid_commands, input_command, int_input=None):
    if valid_commands is None or input_command is None:
        cmd = int_input
        while True:
            try:
                cmd = int(cmd)
            except ValueError:
                cmd = input("Please type an integer value greater than zero: ")
                continue
            if cmd < 1:
                cmd = input("Please type an integer value greater than zero: ")
                continue
            return cmd
    else:
        cmd = input_command
        while cmd not in valid_commands:
            cmd = input("Please type a valid command: ")
        return cmd


def main():
    lower_limit = 1
    current_guess = None
    last_guess = None
    upper_limit = None
    guess_status = None
    guesses_number = 0
    continue_game = "y"
    possible_guesses = ["h", "l", "c"]
    continue_commands = ["y", "n"]
    instructions_prompt = """Number Guesser\n\nIf my guess is too high type "h"\nIf it is too low type "l"\nIf it is correct type "c"\n"""

    print(instructions_prompt)

    while continue_game == "y":
        upper_limit = input("Input the desired upper limit: ")

        upper_limit = check_valid_input(None, None, upper_limit) + 1

        print("It will take at most {} guesses :D\n".format(
            ceil(log(upper_limit, 2))))

        while guess_status is None or guess_status != "c":
            guesses_number += 1

            sum_of_limits = upper_limit + lower_limit

            current_guess = (sum_of_limits) // 2

            guess_limits = last_guess == upper_limit or last_guess == lower_limit or lower_limit == upper_limit-1

            if upper_limit - lower_limit <= 2 and guess_limits:
                print("The number is {}".format(current_guess))
                break

            guess_status = input("Is the number {}?: ".format(current_guess))

            guess_status = check_valid_input(
                possible_guesses, guess_status.lower())

            if guess_status == "l":
                lower_limit = current_guess
            elif guess_status == "h":
                upper_limit = current_guess

            last_guess = current_guess

        print("\nFinally guessed the number! :V")

        print("Total of guesses: {}".format(guesses_number))

        continue_game = input("Do you want to play again? (y/n)")

        continue_game = check_valid_input(
            continue_commands, continue_game.lower())

        guesses_number = 0
        guess_status = None
        lower_limit = 1


if __name__ == "__main__":
    main()
