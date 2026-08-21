def main():
    years = int(input("Enter a number of years into the future: "))
    transistors = 17.8
    current_year = 2026
    
    if (current_year + years) >= 2030:
        print("the law is not valid.")
    else:
        transistors *= 2 ** (years / 2)
        print(transistors, "Billions")

if __name__ == "__main__":
    main()
