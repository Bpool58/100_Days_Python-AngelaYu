def my_function():
    for i in range(1, 20):  #The bug is that it does not reach i =20 because it only steps/stops at 19
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
#    The for loop is iterating through numbers from 1 to 19 (inclusive) using range(1, 20).
#    It creates a sequence that starts at 1 and ends at 19, as range(1, 20) excludes the upper bound 20.
#
# 2. When is the function meant to print "You got it"?
#    The function is meant to print "You got it" when i equals 20. However, this will never happen
#    because the range(1, 20) never reaches 20 - it stops at 19.
#
# 3. What are your assumptions about the value of i?
#    The values of i will be: 1, 2, 3, ..., 18, 19
#    The code assumes i will reach 20, but due to how range() works, i will never equal 20.
#    To fix this, we would need to change range(1, 20) to range(1, 21) if we want to include 20.