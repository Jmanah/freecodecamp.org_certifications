import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    a = np.asarray([[list.pop(0)for i in range(3)]for i in range(3)])
    return {
        'mean': [
            (np.mean(a, axis = 0)).tolist(),
            (np.mean(a, axis = 1)).tolist(),
            np.mean(a)
        ],
        'variance': [
            (np.var(a, axis = 0)).tolist(),
            (np.var(a, axis = 1)).tolist(),
            np.var(a)
        ],
        'standard deviation': [
            (np.std(a, axis = 0)).tolist(),
            (np.std(a, axis = 1)).tolist(),
            np.std(a)
        ],
        'max': [
            (np.max(a, axis = 0)).tolist(),
            (np.max(a, axis = 1)).tolist(),
            np.max(a)
        ], 
        'min': [
            (np.min(a, axis = 0)).tolist(),
            (np.min(a, axis = 1)).tolist(),
            np.min(a)
        ], 
        'sum': [
            (np.sum(a, axis = 0)).tolist(),
            (np.sum(a, axis = 1)).tolist(),
            np.sum(a)
        ], 
    }