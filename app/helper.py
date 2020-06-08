import numpy as np
from app.module.loader import *

def formatRequest(request_hash):
    rgba_hash = request_hash["pixel_values"]["data"]
    rgba_values = np.array(list(rgba_hash.values()))
    rgb_values = np.reshape(rgba_values, (28, 28, -1))[:, :, :-1]
    grayscale = np.mean(rgb_values, axis = 2)
    return np.reshape(grayscale, (1, -1))

def getPrediction(pixel_array):
    norm_pixel_array = normalise(pixel_array)
    nn_model = getModel()
    pre = nn_model.predict(norm_pixel_array)
    return pre.argmax(axis = 1)[0]

def normalise(pixel_array):
    mean, std = getNormalParams()
    return (pixel_array - mean)/std