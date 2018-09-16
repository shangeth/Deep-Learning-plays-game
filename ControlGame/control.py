import numpy as np
import cv2
import time
from mss import mss
from PIL import Image
import pyautogui

def process_img(orig_img):
	processed_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
	processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
	return processed_img





box = { "top": 45, "left": 0, "width": 500, "height": 340}
sct = mss()

while True:

    t = time.time()
    sct.get_pixels(box)
    image = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    image=np.array(image)
    new_screen = process_img(image)

    # cv2.imshow('test', image)
    cv2.imshow('window', new_screen)
    print('fps: {}'.format(1/(time.time()-t)))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
        