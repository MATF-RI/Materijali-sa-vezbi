import numpy as np

def read_tsp(filename):
    with open(filename, "r") as f:
        lines = f.read().split("EDGE_WEIGHT_SECTION")[1]
        values = lines.split("EOF")[0]

    matrix = np.fromstring(values, sep=" ", dtype=int)

    n = int(np.sqrt(len(matrix)))
    matrix = matrix.reshape((n, n))

    return matrix