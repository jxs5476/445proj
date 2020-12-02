import keras
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


# arr,left point,right point
def plot(arr, lp, rp):
    rp += 1
    subArr = arr[lp:rp]
    plt.plot(subArr)
    plt.show()


point1 = 1
point2 = 3
testArr = [9485.342, 9134.619, 8877.945, 12002.114, 12005.054, 12304.834]
