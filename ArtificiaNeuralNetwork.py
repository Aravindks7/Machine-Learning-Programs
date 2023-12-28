import numpy as np

X np.array([[2, 9], [1, 5], [3, 6]), dtype=float) 
y= np.array(([92], [86], [89]), dtype=float)
X = X/np.amax (X, axis=0) # Normalize 
y = y/100

X

y

def sigmoid(x):
  return 1/(1+ np.exp(-x))
def sigmoid grad(x):
  return x * (1 - x)

# Variable initialization 
epoch=1000
eta =0.2
input_neurons = 2
hidden_neurons = 3
output_neurons = 1
