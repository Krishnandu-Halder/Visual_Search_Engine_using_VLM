import os
from PIL import Image
import numpy as np

import torch
import torch.nn as nn
import torchvision
from torchvision import transforms
#this will read all images
images = os.listdir("/Users/krishnenduhalder/visual search engine for similar search images/images")

#setting a environment for model 
# os.environ["TORCH_HOME"] = "E:\model_weights_edir"

#giving weights
model = torchvision.models.resnet18(weights = "DEFAULT")


#naming some variables for use in purpose
Names = []
Vectors = None

#put the model in evaluation mode
model.eval()

#finally declare a variable call root
root = "./images/"

#images should get in a certain format to analyse 
transform = transforms.Compose([
    #resize all images into a particular size
    transforms.Resize((256 , 256)) ,
    transforms.ToTensor() ,#using for transformation
    transforms.Normalize(mean = [0.485 , 0.456 , 0.406] , std = [0.229 , 0.224 , 0.225])#normalize images with standard deviation and mean
])
#standard way to implement hook
activation = {} #empty dictionary to activate hooks 
def get_activation(name):
    def hook(model , input , output):
        activation[name] = output.detach()
    return hook

model.avgpool.register_forward_hook(get_activation("avgpool")) #we dont want this into the last step so we will hook this into second last step

with torch.no_grad(): #generating feature vector 
    for i , file in enumerate(images):
        try:
            img = Image.open(root + file)
            img = transform(img)
            out = model(img[None , ...])
            vec = activation["avgpool"].numpy().squeeze()[None , ...]
            if Vectors is None:
                Vectors = vec
            else:
                Vectors = np.vstack([Vectors , vec])
            Names.append(file)
        except:

            continue
        if i % 100 == 0 and i != 0:
            print(i , "done")

np.save("Vectors.npy" , Vectors)
np.save("Names.npy" , Names)










