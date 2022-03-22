import math
from random import randint
import sys
from PIL import Image


imagePath = sys.argv[1]
goalWidth = int(sys.argv[2])
goalHeight = int(sys.argv[3])
goalAspectRatio = goalWidth / goalHeight

with Image.open("in/" + imagePath) as baseImage:
    baseWidth = baseImage.width
    baseHeight = baseImage.height
    baseAspectRatio = baseWidth / baseHeight
    template = Image.new(size=(goalWidth, goalHeight), color=(255, 255, 255), mode="RGB")
    newWidth = 0
    newHeight = 0
    # get the size we are going to change the image to 
    # make the longer side the side that is sized down to its corresponding size
    if (baseWidth > baseHeight):
        newWidth = goalWidth
        newHeight = newWidth / baseAspectRatio
    else:
        # height is longer
        newHeight = goalHeight
        newWidth = newHeight * baseAspectRatio
    
    # now resize the image and put it on the template
    goalImage = baseImage.resize(size=(int(newWidth), int(newHeight)))
    template.paste(goalImage, box=(int(goalWidth / 2 - newWidth / 2), int(goalHeight / 2 - newHeight / 2)))
    # save
    template.save("out/" + imagePath + "-" + str(randint(0, 1000)) + "-SIZED.jpeg")

