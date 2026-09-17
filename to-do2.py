def main():
    # fruits = ["apple", "banana", "cherry"]
    # print("banana" not in fruits)
    # print("pineapple" in fruits)
    # fruit = "apple"
    # print("a" in fruit)

    mission = []
    while True:
        print(f"Missions to do: {len(mission)}")
        print(mission)

        newmission = input("Mission: ").capitalize().strip()

        if newmission == "Exit":
            break
        elif newmission not in mission:
            mission.append(newmission)
        elif newmission in mission:
            del_confirm = input(f"Did you completed {newmission}? (y / n ): ").lower().strip()
            if del_confirm == "y":
                mission.remove(newmission)
            else:
                continue









if __name__ == "__main__":
    main()
