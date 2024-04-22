from PIL import Image,ImageDraw
#makes an image
def make_img_arr(filename):
    image = Image.open(filename)
    imgArr = [image]
    for i in range (1, 90):
        imgArr.append(image.rotate(i*2))
    return imgArr
    
#takes an image array and saves it as a GIF file
def make_gif(imgArr):
    frame_one = imgArr[0]
