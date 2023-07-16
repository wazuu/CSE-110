from PIL import Image

image_background = Image.open("earth.jpg")
pixels_background = image_background.load()
image_foreground = Image.open("spaceshuttle.jpg")
pixels_foreground = image_foreground.load()

width, height =image_background.size

image_combined = Image.new("RGB", (width, height))
pixels_combined =image_combined.load()

print(pixels_foreground[0,0])

for y in range(0, height):
    for x in range(0, width):
        red, green, blue = pixels_foreground[x,y]
        
        if red < 150 and green > 150 and blue < 150:
            red, green, blue = pixels_background[x,y]

        pixels_combined[x,y] = (red, green, blue)

image_combined.show()



