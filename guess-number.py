import random

def main():
    nombre = input("Hello!, can I know who are you? ").title().strip()
    




    print(f"Well, {nombre}, I am thinking of a number between 1 and 100, why you don't try to guess it?")

    num = random.randint(1,100)
    guess = 45

    while guess != num:
        guess = int(input("Why you don't try to guess it: "))
        if guess > num:
            print("That's too big, why you don't try to guess it: ")
        elif guess < num:
            print("That's too small, why you don't try to guess it: ?")
    print(f"Great job, {nombre}, you could guess my number")


if __name__ == "__main__":
    main()
