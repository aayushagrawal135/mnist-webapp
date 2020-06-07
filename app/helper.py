import numpy as np

def formatRequest(request_hash):
    rgba_hash = request_hash["pixel_values"]["data"]
    rgba_values = np.array(list(rgba_hash.values()))
    rgb_values = np.reshape(rgba_values, (28, 28, -1))[:, :, :-1]
    grayscale = np.mean(rgb_values, axis = 2)
    return np.reshape(grayscale, (1, -1))
