import ctypes
import time

from PIL import Image

# ctypes.windll.user32.SystemParametersInfoW(20, 0, "absolute path", 0)

#get images
#get time

#get weather data

starttime = time.time()

while True:

    

    ctypes.windll.user32.SystemParametersInfoW(20, 0, prepaired_image, 0)
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))