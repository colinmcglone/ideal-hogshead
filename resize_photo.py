from PIL import Image
from os import listdir

im_list = [f for f in listdir('./') if f.endswith(".png")]

print(im_list)

for im in im_list:
    with Image.open(im) as i:
        i.thumbnail([1920,1080], Image.ANTIALIAS)
        i.save('reduced_' + im)

print('Done!')
sleep(500)