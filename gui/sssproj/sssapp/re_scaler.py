import numpy as np
from sklearn.preprocessing import MinMaxScaler
def rescale_gui_input(data):
    data_reshaped = np.array(data).reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    rescaled_data = scaler.fit_transform(data_reshaped)

    return rescaled_data.flatten()


