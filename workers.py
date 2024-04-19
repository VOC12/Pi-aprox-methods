import numpy as np

def worker(args):
    xi, delta_x = args
    return np.sqrt(1 - xi**2) * delta_x
