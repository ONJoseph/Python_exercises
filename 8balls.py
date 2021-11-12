"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.

Prompt the user- 
generate randomized answer
    create a list of possible answers
    randomly select
give answer
"""
import random

ANSWER1 = 'Yes'
ANSWER2 = "Absolutely Not"
ANSWER3 = 'Sure'
ANSWER4 = 'Most Likely'

def main():
    # Fill this function out!
    prompt = input("Enter your questions yes or no format: ")
    while prompt != "": 
        give_random_answer()
        prompt = input("Enter your questions yes or no format: ")


def give_random_answer(): 
    answer = random.randint(1,4)
    if answer == 1:
        print (ANSWER1)
    if answer == 2:
        print (ANSWER2)
    if answer == 3:
        print (ANSWER3)
    if answer == 4:
        print (ANSWER4)
    

if __name__ == "__main__":
    main()
