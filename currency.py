def main():
    CO = float(input("What do you have left in pesos? "))
    PE = float(input("What do you have left in soles? "))
    BR = float(input("What do you have left in reais? "))

    mxn = (CO * 0.0054) + (PE * 5.07) + (BR * 3.28)
    usd = mxn / 17.06

    print("MXN: ", round(mxn, 2))
    print("USD: ", round(usd, 2))

if __name__ == "__main__":
    main()
