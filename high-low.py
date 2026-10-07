def main():
    def higuest(a, b):
        if a > b:
            print(a)
        else:
            print(b)

        x = int(input("Enter number for x: "))
        y = int(input("Enter number for y: "))
        print(f"{x} is higuest than {y}")

    higuest(x, y)

if __name__ == "__main__":
    main()
