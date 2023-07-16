from PIL import Image
image_beach = Image.open("beach.jpg")
image_beach.show()
print(image_beach.size)
pixels_beach = image_beach.load()
print(pixels_beach[400, 200])
pixels_beach[400, 200] = (255, 0, 255)
pixels_beach[401, 200] = (255, 0, 255)
pixels_beach[402, 200] = (255, 0, 255)
pixels_beach[403, 200] = (255, 0, 255)
pixels_beach[404, 200] = (255, 0, 255)


image_beach.show()