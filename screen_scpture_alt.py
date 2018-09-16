import numpy as np
import cv2
import time
from mss import mss
from PIL import Image

box = { "top": 45, "left": 0, "width": 500, "height": 340}
sct = mss()

while True:

    t = time.time()
    sct.get_pixels(box)
    image = Image.frombytes('RGB', (sct.width, sct.height), sct.image)

    cv2.imshow('test', np.array(image))
    print('fps: {}'.format(1/(time.time()-t)))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
        