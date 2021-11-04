import cv2
import numpy as np
from PIL import Image

class ImageLoader:
    
    def __init__(self):
        self.im1 = Image.open("images/test.jpg", 'r')
        self.im1data = self.load_image(self.im1);
        
    def load_image(self ,imfile):
        pix_val = np.array(imfile.getdata())
        return pix_val;

    def develop_image(self, sliceimage):
        out = Image.open("images/layerout.jpg");
        out.putdata(sliceimage);
        out.show()
