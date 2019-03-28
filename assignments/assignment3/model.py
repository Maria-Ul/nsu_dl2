import numpy as np

from layers import (
    FullyConnectedLayer, ReLULayer,
    ConvolutionalLayer, MaxPoolingLayer, Flattener,
    softmax_with_cross_entropy, l2_regularization
    )

class ConvNet:
    """
    Implements a very simple conv net

    Input -> Conv[3x3] -> Relu -> Maxpool[4x4] ->
    Conv[3x3] -> Relu -> MaxPool[4x4] ->
    Flatten -> FC -> Softmax
    """
    def __init__(self, conv1_size, conv2_size, reg):
        self.reg = reg
        # TODO Create necessary layers
        raise Exception("Not implemented!")   
 
    def compute_loss_and_gradients(self, X, y):
        # TODO Compute loss and fill param gradients
        # Don't worry about implementing L2 regularization, we will not
        # need it in this assignment
        raise Exception("Not implemented!")   
 
    def predict(self, X):
        # You can probably copy the code from previous assignment
        raise Exception("Not implemented!")   

    def params(self):
        result = {}

        # TODO: Aggregate all the params from all the layers
        # which have parameters
        raise Exception("Not implemented!")
    
        return result
