import numpy as np

def calculate(data):

    if len(data) != 9:
      raise ValueError ("List must contain nine numbers.")
       
    arr = np.array(data)
    matrix = arr.reshape(3,3)
  
    calculations = {
      'mean': [matrix.mean(axis = 0).tolist(), matrix.mean(axis = 1).tolist(), np.mean(arr)],

      'variance': [matrix.var(axis = 0).tolist(), matrix.var(axis = 1).tolist(), np.var(arr)],

      'standard deviation': [matrix.std(axis = 0).tolist(), matrix.std(axis = 1).tolist(), np.std(arr)],

      'max': [matrix.max(axis = 0).tolist(), matrix.max(axis = 1).tolist(), np.max(arr)],

      'min':[matrix.min(axis = 0).tolist(), matrix.min(axis = 1).tolist(), np.min(arr)],

      'sum': [matrix.sum(axis = 0).tolist(), matrix.sum(axis = 1).tolist(), np.sum(arr)]
      
    }
  
    return calculations
   