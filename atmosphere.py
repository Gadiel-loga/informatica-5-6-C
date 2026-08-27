def main():

    layers = input(""Descend atmosphere layer: ": ").title().strip()

    if layers == "Exosphere":
        ad = "700–10,000 km"
        print("your altitude level will be between",ad)

    if layers == "Thermosphere":
        ad = "85–700 km"
        print("your altitude level will be between",ad)

    if layers == "Mesosphere":
        ad = "50–85 km"
        print("your altitude level will be between",ad)

    if layers == "Stratosphere":
        ad = "12–50 km"
        print("your altitude level will be between",ad)

    if layers == "Troposphere":
        ad = "0–12 km"
        print("your altitude level will be between",ad)

    altitude = int(input("Enter exact altitude: "))

    if altitude <= 700:
        descend = altitude * 10
        time = (230.0 + 175.0 + 506.7 + 600.0)
        descend2 = descend / time





if __name__ == "__main__":
    main()
