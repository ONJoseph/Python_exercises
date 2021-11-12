"""
Prints the Fizz Buzz sequence up to a given number.
1) get number
2) check if it is divisible by 3
3) check if it is divisible by 5
4) determine whether it is divisible by 3, 5, or both
5) print fizz, buzz, or fizzbuzz
"""

def main():
    # Fill this function out!
    number_to_count = int(input("Enter the number to count: "))
    for i in range(1, number_to_count+1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
 
if __name__ == '__main__':
    main()
