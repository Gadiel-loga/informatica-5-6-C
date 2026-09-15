def main():
    mission = ["find a cat", "feed the cat", "play with the cat", "give the cat a bath", "feed x2 the cat", "put the cat to sleep"]
    new_mission = ""
    while True:
        print(f"You have {len(mission)} missions to do.")
        print(mission)
        command = input("What do you want to do? (add, complete or stop): ").lower()
        if command == "add":
            new_mission = input("New mission: ")
            mission.append(new_mission)
        elif command == "stop":
            break


if __name__ == "__main__":
    main()
