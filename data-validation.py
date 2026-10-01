def main():
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number between 1 and 10: "))

            not_validated = False # -> break
            if number >= 1 and number <=10:
                print("Number stored successfully.")
            else:
                print("A NUMBER BETWEEN 1 AND 10")
        except ValueError:
            print("YOU DIDN'T ENTERED A NUMBER!")
    # ctrl + k + c / ctrl + k + u
    while True:
        try:

            name = input("Enter your name: ")
            f_letter = name[0]
            print("Name stored succesfully.")
            break
        except IndexError:
            print("A name is required")



if __name__ == "__main__":
    main()

