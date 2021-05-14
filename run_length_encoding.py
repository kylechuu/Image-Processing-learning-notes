import numpy as np

class Rle:
    def __init__(self):
        pass

    def encode_image(self, binary_image):
        """
        For efficiency, flatten the image by concatinating rows to create long array.
        Compute run length encoding on the long array.
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        height, width = binary_image.shape
        rle_code = ['0' if not binary_image[0][0] else '1']
        number = 0
        color = binary_image[0][0]

        for row in range(height):
            for col in range(width):
                if binary_image[row][col] == color:
                    number += 1
                else:
                    rle_code.append(number)
                    number = 1
                    color = binary_image[row][col]
        if number:
            rle_code.append(number)

        return rle_code

    def decode_image(self, rle_code, height, width):
        """
        Since the image was flattened during the encoding, use the hight and width to reconstruct the image
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """

        image = np.zeros((height, width), np.uint8)
        row = col = color = 0
        if rle_code[0] == '1':
            color = 255

        for index in range(1, len(rle_code)):
            for _ in range(rle_code[index]):
                image[row][col] = color
                col += 1
                if col == width:
                    row += 1
                    col = 0


            if color != 0:
                color = 0
            else:
                color = 255


        return image




        




