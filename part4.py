from PIL import Image,ImageDraw
#makes an image
def make_img_arr():
    imgArr = [Image.open("star2.png"),Image.open("zoomed.png"),
              Image.open("cc90.png"),Image.open("upside_down.png"),
              Image.open("reflected.png"),Image.open("reflect3.png"),
              Image.open("sheared.png")]
    return imgArr
    
#takes an image array and saves it as a GIF file
def make_gif(imgArr):
    frame_one = imgArr[0]
    frame_one.save("star_rotation1.gif", format="GIF", append_images=imgArr,
               save_all=True, duration=100, loop=0)
make_gif(make_img_arr)