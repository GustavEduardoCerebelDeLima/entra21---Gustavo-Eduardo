from PIL import Image, ImageDraw

# im = Image.open("1massa.jpg")
# im = im.convert("RGB")
# x, y = im.size
#
# for i in range(x):
#     for j in range(y):
#         r, g, b = im.getpixel((i, j))
#         r = 255 - r
#         g = 255 - g
#         b = 255 - b
#         im.putpixel((i, j), (r, g, b))
# d_im = ImageDraw.Draw(im)
# im.show()

# im = Image.new("RGB",(1080,720), (255,255,255))
# # im.show()
# im2 = Image.new("RGB",(240,600), (0,0,255))
# # im2.show()
# im3 = Image.new("RGB",(240,600), (255,0,0))
# x,y = im.size
# im.paste(im2,(x//2-480,y//2-300))
#
# im.paste(im3,(x//2+480,y//2+300))
# im.show()

im = Image.open("rosamama.jpg")

im2 = im.convert("P")

x,y = im2.size

for i in range(x):
    for j in range(y):
        P = im.getpixel((i, j))
        print(P)

im2.show()


