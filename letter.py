def main():
    receivers = ["Mario", "Luigi", "Daisy", "Yoshi", "Toad", "Princess Peach", "Bowser"]

    for character in receivers:
        if receivers != "Princess Peach":
            print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {character},

       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {receivers[5]}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """)





if __name__ == "__main__":
    main()
