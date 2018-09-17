#Show menu and let user choose
def menu():
    print("""What would you like to check?
    
    (1) Exercises...
    (2) Repetitions max weight...
    (3) Metabolic rate...
    """)

    #Let the user input a number to choose what function to start
    answer = input("Enter your choice: ")

    if answer == "1":
        print("Exercises")
    elif answer == "2":
        return rmCheck()
    elif answer == "3":
        return mrCheck()

#Check user's metabolic rate by his body stats
def mrCheck():


    gender = str(input("What is your gender? (M/F)")).lower().strip()
    if gender[0] == 'm':
        gender = 5
        print('Gender: Male')
    elif gender[0] == 'f':
        gender = -161
        print('Gender: Female')
    else:
        print('Invalid input.')


    #!!!MAKE THOSE AS SEPARATE FUNCTIONS???
    age = input("What is your age?")

    try:
        userAge = int(age)
        userAge = userAge * 5
        print(userAge)

    except ValueError:
        print('Invalid input')



    weight = input("What is your weight? (in kilograms)")

    try:
        userWeight = int(weight)
        userWeight = weight * 10
        print(userWeight)

    except ValueError:
        print('Invalid input')


    height = input("What is your height? (in centimeters)")

    try:
        userHeight = int(height)
        userHeight = height * 6.25
        print(userHeight)

    except ValueError:
        print('Invalid input')

    #Calculate the BMR here
    bmr = int(gender + userWeight + userHeight - userAge)
    print('Your Basal Metabolic Rate is:', bmr, ' calories')


#Check user's max weight for different repition ranges
def rmCheck():
    #Take users's rm1 weigth to use in the calculations
    weight = input("What is your RM1?")

    #Calculate different RM, make is a float, and display only two digits after decimal
    try:
        rm = float(weight)
        print("Your RM1 is: ", rm)

        for i in range(2, 11):
            rm -= rm * 0.05
            num = float("{0: .2f}".format(rm))
            print("Your RM%s is: " %(i), num)
        print()
        askUser()

    #If user inserted invalid input, return to rmCheck function
    except ValueError:
        print("That's not a number, try again.")
        rmCheck()


#Ask the user if he wants to check another RM, if not then return to menu(), if invalid input return to askUser()
def askUser():
    check = str(input("Check another number? (Y/N): ")).lower().strip()

    try:
        if check[0] == 'y':
            return rmCheck()
        elif check[0] == 'n':
            return menu()
        else:
            print('Invalid input.')
            return askUser()

    except ValueError:
        print("Please enter valid input.")
        return askUser()


menu()
