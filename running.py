"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.

1. take input from the user
2. 
"""

def main():
    # Fill this function out!
    user_input = int(input("Enter number: "))
    total = user_input
    minimum = user_input
    maximum = user_input

    while user_input != 0:
        print(total)
        user_input = int(input("Enter number: "))
        if user_input < minimum:
            minimum = user_input
        if user_input > maximum: 
            maximum = user_input
        total += user_input # num = num + user_input
        
    print ("The maximum value so far was " + str(maximum))
    print ("The minumum value so far was " + str(user_input))
    
if __name__ == '__main__':
    main()
