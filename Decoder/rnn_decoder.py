# Get access to parent directory
import os, sys
sys.path.append(os.path.dirname(os.getcwd()))

# Imports
import tensorflow as tf


class RNNDecoder(tf.keras.Model):
    def __init__(self, units):
        """
            units:      number of internal units per layer
        """
        super(RNNDecoder, self).__init__()
        
        # TODO
        
        pass

