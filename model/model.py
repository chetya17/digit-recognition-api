import pickle
from pathlib import Path
import cv2
import numpy as np




with open("/rfc.pkl", "rb") as f:
    model = pickle.load(f)


def predict_pipeline(text):
    test_image = cv2.imread(text, cv2.IMREAD_GRAYSCALE)
    img_resized = cv2.resize(test_image, (28, 28), interpolation=cv2.INTER_LINEAR)
    img_resized = cv2.bitwise_not(img_resized)
    img_resized = np.array(img_resized)
    img_resized = img_resized.reshape(1,784)
    
    pred = model.predict(img_resized)
    return pred