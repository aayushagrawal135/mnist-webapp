import json
import os
from .functions import *
from app import app

class JsonParams():
    def __init__(self, filename = None):
        self.filename = os.path.join("app/static/data", filename or "nn_params.json")

    def dumpParamsInJson(self, model):
        params = dict()
        for layer in model.layers:
            if type(layer) is Linear:
                params[f"{layer}_weights"] = layer.weights.tolist()
                params[f"{layer}_bias"] = layer.bias.tolist()

        with open(self.filename, "w") as file:
            json.dump(params, file)


    def loadParamsIntoLayers(self, layers):
        with open(self.filename, "r") as file:
            params = json.load(file)

        for layer in layers:
            if type(layer) is Linear:
                key_weight = f"{layer}_weights"
                key_bias = f"{layer}_bias"
                layer.setWeights(np.array(params[key_weight]))
                layer.setBias(np.array(params[key_bias]))
        
        return layers

    def dumpNormaliseParams(self, mean, std):
        params = dict()
        params["mean"] = mean
        params["std"] = std

        with open(self.filename, "w") as file:
            json.dump(params, file)

    def loadNormalParams(self):
        with open(self.filename, "r") as file:
            params = json.load(file)

        return params["mean"], params["std"]