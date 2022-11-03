import keras
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
from keras import backend as K

def f1_score(y_true, y_pred): 
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
    return f1_val

def teachable_machine_classification(img, weights_file):
    # Load the model
    model = keras.models.load_model(weights_file, custom_objects={"f1_score": f1_score})

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 48,48), dtype=np.float32)
    image = img
    #image sizing
    size = (48,48)
    
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return np.argmax(prediction) # return position of the highest probability