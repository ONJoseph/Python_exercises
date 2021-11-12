from karel.stanfordkarel import *

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""

def main():
    for i in range(2):
        while front_is_clear():
            put_twenty_beepers()
            move()
            put_twentyone_beepers()
            move()
        
#places 20 beepers using for loop
def put_twenty_beepers():
    for i in range(20):
        put_beeper()
#places 21 beepers using for loop
def put_twentyone_beepers():
    for i in range(21):
        put_beeper()
    
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """


if __name__ == '__main__':
    run_karel_program()
