def main():
    print("Halo user, welcome to the Times Table Generator")
    times_table = int(input("Enter a times table that you would like to be tested on: "))
    max_value = int(input("Enter the maximum value for your times table: "))
    range(max_value)
    if 1 <= times_table:
        print(f"Here is the {times_table} times table")

        for x in range(1, max_value + 1):
            answer = x * times_table
            print(f"{x} times {times_table} is {answer}")
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
