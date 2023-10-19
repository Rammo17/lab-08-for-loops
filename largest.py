highestnum = 0
for i in range(0, 4, 1):
    userInput = input("Number please...")
    userInt = int(userInput)
    print("User enterred: " + str(userInput))
    if userInt > highestnum:
        highestnum = userInt
        print("Updating highest number...")
    else:
        print("This is not the highest number!")
print("The highest number enterred is: " + str(highestnum))
           