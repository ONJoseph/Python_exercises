from simpleimage import SimpleImage

def main():
    image = SimpleImage('prague.jpg')
    trimmed_img = trim_crop_image(image, 20)
    trimmed_img.show()


def trim_crop_image(image, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_size pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_size is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side
                   of the original image

    Returns:
        A new SimpleImage with trim_size pixels shaved off each
        side of the original image
    """
    new_height = image.height - (2 * trim_size)
    new_width = image.width - (2 * trim_size)
    trimmed_image = SimpleImage.blank( new_width, new_height)
    
    for y in range (new_height): 
        for x in range (new_width):
            old_x = x + trim_size
            old_y = y + trim_size
            old_pixel = image.get_pixel(old_x, old_y)
            trimmed_image.set_pixel(x, y, old_pixel)

    return trimmed_image



if __name__ == '__main__':
    main()
