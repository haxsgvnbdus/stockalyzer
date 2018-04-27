from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense, Activation


#model info
number_epochs = 10
batch_size = 1 
verbose = 2


model = Sequential()
model.add(LSTM(32, input_shape=(1, step_size), return_sequences = True))
model.add(LSTM(16))
model.add(Dense(1))
model.add(Activation('linear'))

model.compile(loss='mean_squared_error', optimizer='adagrad') # Try out SGD, adam





 


