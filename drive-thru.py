def main():
    welcome()
    choice = int(input("Selectyour order: "))
    get_item(choice)


def welcome():
    menu = ["Pizza", "Mangoneadas", "chilaquiles", "Sodas", "Natural fruit-flavored waters", "Quesabirrias"]
    print("Welcome to ")
    print("Here's is the menu: ")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")



def get_item(order):
    if order == 1:
        print("🍕")🥭🍹🧊🥤
    #kitchen = [""""""""""""]
    #print(kitchen[order - 1])

if __name__ == "__main__":
    main()
