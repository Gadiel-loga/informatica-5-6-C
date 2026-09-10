from datetime import datetime

print("What day is it?")
day = int(input())
day = datetime.now().weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]
print(days [day])

if day <= 4:
    print("It's a weekday")
    remaining = 5 - day
    print(remaining, "days until the weekend")
elif day == 4:
    print("It's Friday")
    print("Just a day until the weekend")
else:
    print("It's the weekend")

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Dicember"]
print("These are the summer months")
print(months[5])
print(months[6])
print(months[7])

month = 
print("It is", months[month-1])
