def main():

    layers = input("Enter the target atmospheric layer: ").title()

    if layers == "Exosphere":
        ad = "700–10,000 km"
        print("The altitude distance range from Earth of the exosphere is",ad)

    if layers == "Thermosphere":
        ad = "85–700 km"
        print("The altitude distance range from Earth of the thermosphere is",ad)

    if layers == "Mesosphere":
            ad = "50–85 km"
            print("The altitude distance range from Earth of the mesosphere is",ad)

    if layers == "Stratosphere":
                ad = "12–50 km"
                print("The altitude distance range from Earth of the stratosphere is",ad)

    if layers == "Troposphere":
                    ad = "0–12 km"
                    print("The altitude distance range from Earth of the troposphere is",ad)

if __name__ == "__main__":
    main()
