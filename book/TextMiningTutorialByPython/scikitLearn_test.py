# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd
iris = load_iris()
species = ['Setosa', 'Versicolour', 'Virginica']
irispddata = pd.DataFrame(iris.data, columns=iris.ffeature_names)
irispdtarget = 
