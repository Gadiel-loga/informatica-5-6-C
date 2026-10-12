def main():
    print("Welcome human to Decimal Converter")
    print("My purpose is to calculate and pass binary numbers to Decimals)")
    valid_bits = ["0", "1"]
    while True:
        correct_chars = 0
        bi = input("Enter your binary number: ")
        for char in bi:
            if char in valid_bits:
                correct_chars += 1
        if correct_chars == len(bi):
            break
        else:
            print("Invalid input.")

    binary_to_decimal(bi)



def binary_to_decimal(binary):
    decimal = 0
    for bit in binary:
        decimal = (decimal * 2) + int(bit)
    print(decimal)

if __name__ == "__main__":
    main()
