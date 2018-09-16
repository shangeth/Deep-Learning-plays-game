import numpy as np
import cv2
import time
from mss import mss
from PIL import Image
from pykeyboard import PyKeyboard
import pyautogui


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)
    except:
        pass


def process_img(orig_img):
    processed_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)
    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500]])
    processed_img = roi(processed_img, [vertices])

    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 200, 3)
    draw_lines(processed_img, lines)

    return processed_img




box = { "top": 45, "left": 0, "width": 800, "height": 600}
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
        