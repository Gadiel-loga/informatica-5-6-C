def main():
    # min, max, sum
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ads = max(num) #highest number
    print(ads)
    ads2 = sum(num) #plus all numbers
    print(ads2)
    ads3 = min(num) #minimum
    print(ads3)

    #sort: ordena segun el orden general
    numbers = [1, 4, 5, 7, 9, 3]
    numbers.sort()
    print(numbers)  #Basado en los primeros numeros

    items = ["Lettuce", "Tomato", "Bread", "Jam", "Mayonaise"]
    items.sort() #Basado en las primeras letras del abecedario
    print(items)

    letters = ["b", "a", "d", "c"]
    letters.sort(reverse=True) #reverse=True 
    print(letters)

    words = ['banana', 'pie', 'apple']
    sorted_words = sorted(words, key=len) #key=len
    print(sorted_words)


    #append and insert
    fruits=["Apple","Orange","Grapes"]
    fruits.append("Banana") #adds to the list
    print(fruits)
    fruits1= ["Apple","Orange","Grapes"]
    fruits1.insert(2, "banana") #inserts in a specific place of the list
    print(fruits1)
    #len al parecer

    mylist = ["pencil", "computer", "shirt", "phone", "paper"]
    print(len(mylist)) #counts items on the list

    list = ["Rojo","amarillo","Verde","naranja","Azul"]
    print("lista", list)

    list.pop(1)
    print("con pop(1):", list)

    list.remove("Rojo")
    print("con remove:",'Rojo')

    numbers = [1, 4, 5, 7, 9, 3]
    numbers.sort()
    print(numbers)

    items = ["Lettuce", "Tomato", "Bread", "Jam", "Mayonaise"]
    items.sort()
    print(items)

    letters = ["b", "a", "d", "c"]
    letters.sort(reverse=True)
    print(letters)

    words = ['banana', 'pie', 'apple']
    sorted_words = sorted(words, key=len)
    print(sorted_words)

    fruits=["Apple","Orange","Grapes"]
    fruits.append("Banana")
    print(fruits)
    fruits1= ["Apple","Orange","Grapes"]
    fruits1.insert(2, "banana")
    print(fruits1)

if __name__ =="__main__":
    main()
