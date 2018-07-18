from random import *

def setup():
    size(346,520)
    
    flowerImage = loadImage("flower.jpg")
    image (flowerImage,0,0)
    loadPixels()

    
# Filter; Remove 1 Color : Blue 
def noColor():
    for r in range (len(pixels)):
        currentPixel = pixels [r]
        pixelRed = red(currentPixel)
        pixelGreen = green (currentPixel)
        pixelBlue = blue (currentPixel)
        #pixelRed = pixelRed  
        #pixelGreen = pixelGreen 
        #pixelBlue =  pixelBlue
        newColor = color(pixelRed, 0, pixelBlue)
        pixels[r] = newColor
    updatePixels()

# Filter Grayscale
def grayScale():
    for r in range (len(pixels)):
        currentPixel = pixels [r]
        pixelRed = red(currentPixel)
        pixelGreen = green (currentPixel)
        pixelBlue = blue (currentPixel)
        average = pixelred + pixelBlue + pixelGreen)/3
        newColor = color(pixelRed, pixelGreen, pixelBlue)
        pixels[r] = newColor(average)
    updatePixels()
