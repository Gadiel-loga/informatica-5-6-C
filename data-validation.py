def main():
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number between 1 and 10: "))
            not_validated = False # -> break
            print("Number stored successfully.")
        except ValueError:
            print("YOU DIDN'T ENTERED A NUMBER!")
if __name__ == "__main__":
    main()

