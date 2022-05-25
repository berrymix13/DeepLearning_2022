import numpy as np
import cv2
from PIL import Image

def center_image(img, src_format = 'OpenCV', dst_format = 'OpenCV', img_size = 224):
    if src_format == 'OpenCV':
        h, w = img.shape[:-1]
    else: # pillow
        h, w = np.array(img).shape[:-1]

    if h > w:
        height, width = (h * img_size)//w , img_size
    else:
        width, height = (w * img_size)//h , img_size

    if src_format == 'OpenCV':
          inter = cv2.INTER_AREA if h + w > 300 else cv2.INTER_CUBIC
          new_img = cv2.resize(img, dsize = (width, height), interpolation = inter)
    else:
            new_img = np.array(img.resize((width, height)))

    diff = abs(width - height) // 2
    if h > w:
        final_img = new_img[diff : diff + img_size, :]
    else:
        final_img = new_img[:, diff : diff + img_size]

    return final_img if dst_format == 'OpenCV' else Image.fromarray(final_img)
