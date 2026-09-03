import random

def main():

    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    nombre = input("Hello!, can I know who are you? ").title().strip()
    print(f"Well, {nombre}, I am thinking of a number between 1 and 100, why you don't try to guess it?.")
        guess = random.choice(num)
        if guess == "1":
            
        elif guess == "2":
        elif guess == "3":
        elif guess == "4":
        elif guess == "5":
        elif guess == "6":
        elif guess == "7":
        elif guess == "8":
        elif guess == "9":
        elif guess == "10":



    faa = ""

        while answer != "Yes!":
            answer = input("Are we there yet? ").strip().title()
            if answer == "Yes":
                followup = input("Really? ").strip().title()
            if followup == "Yes!":
                break







if __name__ == "__main__":
    main()
