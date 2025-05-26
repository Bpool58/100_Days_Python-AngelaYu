# Initialize age with a default value
while True:  # Keep trying until we get a valid input
    try:
        age = int(input("How old are you?"))
        break  # Exit the loop if input is valid
    except ValueError:
        print("You have typed in an invalid number. Please try again with a numerical response such as 15.")

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You are {age} years old and not old enough to drive. You must be over 18.")


