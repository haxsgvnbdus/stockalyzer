from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense, Activation


#model info
number_epochs = 10
batch_size = 1 
verbose = 2
step_size = 1


model = Sequential()
#model.add(LSTM(32, input_shape=(1, step_size), return_sequences = True))
#model.add(LSTM(16))
#model.add(Dense(1))
#model.add(Activation('linear'))

#model.compile(loss='mean_squared_error', optimizer='adagrad') # Try out SGD, adam



def model2(indim, outdim, return_seq):
    
 
    model.add(LSTM(
	return_sequences=return_seq,
        input_shape=(None, indim),
        units=outdim
        ))

    model.add(Dropout(0.2))

    model.add(LSTM(
        128,
        return_sequences=False))

    model.add(Dropout(0.2))
    #model.add(Activation('linear'))
    
    model.add(Dense(
        units=1))
    model.add(Activation('linear'))

    return model


def model1(indim, outdim, return_seq):
     
 
    model.add(LSTM(
	return_sequences=return_seq
        input_shape=(None, indim),
        units=outdim
        ))

    model.add(LSTM(
        100,
        return_sequences=False))

    
    #model.add(LSTM(16))
    #model.add(Dense(1))
    model.add(Dense(
        units=1))
    model.add(Activation('linear'))

    return model

 


