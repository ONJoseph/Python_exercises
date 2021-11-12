"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.
"""

from simpleimage import SimpleImage

BRIGHTNESS_THRESHOLD = 153

def main():
    image = SimpleImage('images/simba-sq.jpg')
    #apply filter 
    for pixel in image: 
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if average >= BRIGHTNESS_THRESHOLD: 
            #grayscale anything that is bright
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    


    image.show()

if __name__ == '__main__':
    main()
