from ImageLoader import ImageLoader
from ConvolutionLayer import ConvolutionLayer
import numpy as np

class network:
    
    def __init__(self):
        self.im_loader = ImageLoader()
        self.layer1 = ConvolutionLayer("conv-layer-bin/L1")

    def predict(self):
        #print("test")
        out = self.layer1.convolve(self.im_loader.im1data, 486, 729)
        out = tuple(map(tuple, out))
        self.im_loader.develop_image(out);
        #print(out)
        
    def ezlayerinit(self):
        mat = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
        self.layer1.add_slice(729, 486, 3, 3, mat)
        self.layer1.save_layer();
        
