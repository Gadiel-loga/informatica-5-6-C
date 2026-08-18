def main():
    width = int(input("Enter the width of the rectangle: "))
    print("O" * width)
    print("O" * width)
    print("O" * width)
    print("O" * width)
    print("O" * width)

    p = (5 * 2) + (width * 2)
    print("Perimeter: ", p)
    a = (width * 5)
    print("Area: ", a)
    d = ((width ** 2) + (5 ** 2) ** 1/2)
    print("Diagonal: ", d)



if __name__ == "__main__":
    main()
