while True:
    try:
        a= int(input("Input a number: "))
        if a>=0:
            raise ValueError("Positive Number- Correct Input Number")
        else:
            raise ValueError("Negative Number-InCorrect Input Number")

    except ValueError as e:
        print(e)