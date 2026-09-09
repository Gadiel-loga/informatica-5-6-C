import random
def main():
    name = input("Hello!, can I know who are you? ").title().strip()
    print(f"Well, {name}, I am thinking of a number between 1 and 100.")

    num = random.randint(1, 100)
    guess = 0

    while guess != num:
        guess = int(input("Why you don't try to guess it? "))
        if guess > num:
            print("That's too big.")
        elif guess < num:
            print("That's too small.")

    print(f"Great job, {name}, you could guess my number")


if __name__ == "__main__":
    main()
