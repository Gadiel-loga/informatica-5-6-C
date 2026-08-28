def main():

    rating = int(input("Eleven Madison Park's stars: "))

    if rating == 5:
        print("Perfection ⭐️⭐️⭐️⭐️⭐️")
    elif rating == 4:
        print("Excellent ⭐️⭐️⭐️⭐️")
    elif rating == 3:
        print("Good ⭐️⭐️⭐️")
    elif rating == 2:
        print("Fair ⭐️⭐️")
    else:
        print("Poor")

    print("Criticism is welcome.")

if __name__ == "__main__":
    main()
