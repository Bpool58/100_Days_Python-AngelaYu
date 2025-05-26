year = int(input("What's your year of birth?")) #For year 1994

if year > 1980 and year < 1994: #Fixed would be "and year <= 1994:"
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")


"""
Nothing prints because nothing equals the input year of 1994
"""



if 1981 <= year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
else:
    print("You are likely a boomer or Gen X.")
