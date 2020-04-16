from PIL import Image

#read the image
im = Image.open("resources/montana.png")

#image size
width = im.size[0]
height = im.size[1]

print(width)
print(height)