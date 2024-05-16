from PIL import Image

img = Image.open('C:/workspace/free.png')
box = (28, 3, 70, 79)
crop_img1 = img.crop(box)

drop = (5, 5, 47, 81)
img.paste(crop_img1, drop)
img.show()

