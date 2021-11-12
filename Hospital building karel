from karel.stanfordkarel import *

# File: HospitalKarel.py
# -----------------------------
# Collaborate with your Section here

# Annie is writing a comment! It works!!

def main():
    while front_is_clear():
        if beepers_present():
            build_hospital()
        
        if front_is_clear():
            move()

def build_column():
    """
    precondition: Karel is facing where the columns aims
    """
    for i in range(2):
        if beepers_present():
            pick_beeper()
        put_beeper()
        move()
    put_beeper()

def build_hospital():
    """
    postcondition: Karel is facing east
    """
    turn_left()
    build_column()
    turn_right()
    move()
    turn_right()
    build_column()
    turn_left()

    
def turn_right(): 
    for i in range(3):
        turn_left()

def turn_around(): 
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    run_karel_program('HospitalKarel2.w')
