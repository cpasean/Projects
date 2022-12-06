import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds
import numpy as np
import argparse
from PIL import Image
import json

parser = argparse.ArgumentParser(description='Image Classifiler_flower')

parser.add_argument("--filepath", type=str, help='Filepath (./test_images/wild_pansy.jpg)')
parser.add_argument("--model" , type=str, help='Model (my_model.h5)')
parser.add_argument("--top_K", type=int, help='Classes per possibility to show from the top rank')

arg = parser.parse_args()
print(arg.filepath, arg.model, arg.top_K)

# pass the arguments
image = arg.filepath
model = arg.model
top_K = arg.top_K

# model loading
model = tf.keras.models.load_model(model, custom_objects={'KerasLayer': hub.KerasLayer}, compile=False)

# get class names from json file
with open('label_map.json', 'r') as f:
    class_names = json.load(f)

# define image size and batch
image_size = 224
batch_size = 64
    
# image file normalize 
def process_image(image):
    
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, (image_size, image_size))
    image /= 255
    return image.numpy()

# predict and return possibilty & classes 
def predict(image_path, model, top_K):
    im = Image.open(image_path)
    test_image = np.asarray(im)
    processed_test_image = process_image(test_image)
    prob_predict = model.predict(np.expand_dims(processed_test_image,axis =0))
    probabilities = np.sort(prob_predict)
    top_prob = probabilities[0][-top_K:][::-1].tolist()
    top_classes = prob_predict.argsort()[0][-top_K:][::-1]
    top_classes = [i for i in top_classes]
    print(top_prob, top_classes)

    
if __name__ == '__main__':
    predict(image, model, top_K)




