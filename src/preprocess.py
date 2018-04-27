import numpy as np
import math
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


#split into training/testing sets 
def split(dataset, barrier): 	#barrier usually 75/25
	train_size = int(len(dataset)*barrier)
	test_size = len(dataset) - train_size

	train_set = dataset[0:train_size, :]
	test_set = dataset[train_size:len(dataset),:]	

	return train_set, test_set


def preprocess(dataset, step): 
	x, y = [], []
	for i in range(len(dataset)-step-1):
		tmp = dataset[i:(i+step)]
		x.append(tmp)
		y.append(dataset[i+step]
	
	return np.array(x), np.array(y)



def select_fields(dataset, list_f):
	tmp = dataset[list_f]
	newset_avg = tmp.mean(axis=1)	#average of all counted columns 
	
	return newset_avg   


def normalize(dataset):
	
	#use standard normalization from sklearn [0,1] 
	
	tmp = np.reshape(dataset, (len(dataset),1))
	scaler = MinMaxScaler(feature_range=(0, 1))
	output = scaler.fit_transform(tmp)

	print output
	return output
	
