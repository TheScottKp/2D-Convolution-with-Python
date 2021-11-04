import os.path
import numpy as np

class ConvolutionLayer():
    def __init__(self, dataPath):
        self.numLayers = 0;
        self.data_path = dataPath
        if (not os.path.isfile(self.data_path)):
            print("File was not found. Check again path or add slice to create new file.")
        else:
            with open(dataPath, 'rb') as f:
                self.numLayers = np.array(np.load(f))[0]
                self.kernel = np.zeros((self.numLayers, 3, 3))
                for x in range(self.numLayers):
                    #self.slice[x] = np.array(np.load(f))
                    self.kernel[x] = np.array(np.load(f))
            
    def add_slice(self, height, width, kheight, kwidth, kernel):
        if (not os.path.isfile(self.data_path)):
            self.slice = np.empty((height, width))
            self.kernel = np.empty((kheight, kwidth))
        #self.slice = np.stack((np.zeros((height, width)),self.slice))
        self.kernel= np.stack((kernel,self.kernel))
        self.numLayers += 1
        
    def save_layer(self):
        with open(self.data_path, 'wb') as f:
            np.save(f,np.array([self.numLayers]))
            for x in range(self.numLayers):
                #np.save(f, self.slice[x])
                np.save(f, self.kernel[x])

    def convolve(self, imdata, height, width):
        kcounter = 0
        jcounter = 0
        output = np.zeros((len(imdata), 3)).astype(int)
        for y in range(width + 1, width*height-width-1, width):
            for x in range(width-2):
                jcounter = 0
                s=0;
                for j in range(-width, 2*width, width):
                    kcounter = 0
                    for k in range(-1, 2, 1):
                        s =+ self.kernel[0][jcounter][kcounter]*imdata[x+y+j+k][2]
                        kcounter=kcounter+1
                    
                    jcounter = jcounter + 1
                    
                output[y+x][0] = -int(s)
                output[y+x][1] = -int(s)
                output[y+x][2] = -int(s)
        return output

