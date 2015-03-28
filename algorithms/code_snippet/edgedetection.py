from PIL import ImageFilter
from convex import convex_hull
from PIL import Image


imageFile ='test2.jpg'

im = Image.open(imageFile)
im1 = im.convert("L")


# Edge Detection
im2 = im1.filter(ImageFilter.Kernel((3, 3),(-1, -1, -1,-1,8,-1,-1, -1, -1),0.3))

px = im2.load()


# Extract the points from the edge
whitepoints = [];

width,height = im2.size
for i in range(width):
    for j in range(height):
        if px[i,j]== 255.0:
            whitepoints.append((i,j))
        else:
            px[i,j] = 0.0

im2.show()

# filter out the points contained in the shape
left = [width-1]*height
right = [0]*height
top = [height -1]*width
bottom = [0]*width
for x,y in whitepoints:
    if x<=left[y]:
        left[y] = x
    if x>=right[y]:
        right[y] = x
    if y <= top[x]:
        top[x] = y
    if y >= bottom[x]:
        bottom[x] = y

for x,y in whitepoints:
    if left[y]<x and x<right[y] and top[x]<y and y<bottom[x]:
        px[x,y] = 0.0
    #print left,right,top,bottom
    
im2.show()
#----Apply filter

