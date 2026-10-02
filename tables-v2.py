def main():
    print("Halo user, welcome to the Times Table Generator")
    while True:
        try:
            times_table = int(input("Enter a times table from 1 to 10: "))
            break
        except ValueError:
            print("An error has occured, try again.")
    while True:
            try:
                max_value = int(input("Enter the maximum value for your times table: "))
                break
            except ValueError:
                print("An error has occured, try again.")
                range(max_value)
            if times_table >= 1 and times_table <=10:
                print(f"Here is the {times_table} times table")
                while True:
                    for x in range(1, max_value +1):
                        try:
                            answer = x * times_table
                            print(f"{times_table} times {max_value} is equal to: ")
                            user = int(input())
                            print(f"{x} times {times_table} is {answer}")
                            print("Correct")
            else:
                print("Invalid command.")


if __name__ == "__main__":
    main()
