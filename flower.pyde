from random import *

def setup():
    size(346,520)
    
    flowerImage = loadImage("flower.jpg")
    image (flowerImage,0,0)
    loadPixels()

    
# Filter; Remove 1 Color : Blue 
    for r in range (len(pixels)):
        currentPixel = pixels [r]
        pixelRed = red(currentPixel)
        pixelGreen = green (currentPixel)
        pixelBlue = blue (currentPixel)
        pixelRed = pixelRed  
        pixelGreen = pixelGreen 
        pixelBlue =  0
        newColor = color(pixelRed, pixelGreen, pixelBlue)
        pixels[r] = newColor
    updatePixels()
