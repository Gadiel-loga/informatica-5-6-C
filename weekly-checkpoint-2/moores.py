def main():
    years = int(input("Enter a number of years into the future: "))
    transistors = 17.8
    transistors *= 2 **  (years / 2)
    print(transistors, "Billions")




if __name__ == "__main__":
    main()
