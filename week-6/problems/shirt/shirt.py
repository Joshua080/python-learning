import sys
from PIL import Image, ImageOps

if len(sys.argv) == 3:

    first = sys.argv[1][-5:].lower()
    second = sys.argv[2][-5:].lower()

    if (first[-4:] == ".png" or first == ".jpeg" or first[-4:] == ".jpg"):
        if (second[-4:] == ".png" or second == ".jpeg" or second[-4:] == ".jpg"):
            if first.split(".")[-1] != second.split(".")[-1]:
                sys.exit("Input and output extensions do not match")
            try:

                im = Image.open(sys.argv[1], "r")
                shirt = Image.open("shirt.png").convert("RGBA")
                im_resized = ImageOps.fit(im, shirt.size)
                im_resized.paste(shirt, (0, 0), mask=shirt)
                im_resized.save(sys.argv[2])

            except FileNotFoundError:
                sys.exit("Image was not found")

        else:
            sys.exit("Please make sure your files are either PNGs or JPEGs")

    else:
        sys.exit("Please make sure your files are either PNGs or JPEGs")

else:
    sys.exit("Please enter two command line arguements")
