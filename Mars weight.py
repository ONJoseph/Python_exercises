"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.

get input of Earth wieght
Convert
Export Mars weight
"""

CONVERSION_RATIO = 0.378

def main():
    # Fill this function out!
    take_input = input("Enter your earth weight: ")
    earth_weight = float(take_input)
    mars_weight = CONVERSION_RATIO * earth_weight
    mars_weight_text = str(mars_weight) 
    print ("The equivalent weight on Mars is: " + mars_weight_text)

if __name__ == "__main__":
    main()
