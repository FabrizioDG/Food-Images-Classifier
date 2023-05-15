import os
import cv2
import numpy as np

TRAIN_PATH = "../data/train_set/"
TEST_PATH = "../data/test_set/"
HEIGHT = 128
WIDTH = 128
BATCH_SIZE = 128
CLASS_NAMES = os.listdir(TRAIN_PATH)

def read_data(path, im_size, class_names_label):
    '''
    This function is used to load images of the different classes in the test dataset. Pictures of each class
    must be organized in subfolders with the name of the corresponding class.

    Input:
    path : string
       The path where the test_set is stored
    im_size: tuple of int
       The Height and Width of the images
    class_names_label: dict
       A dictionary with names of the classes as key and an integer index as values
    
    Output:
       X: numpy array
          Array with the images
       y: numpy array
          Array with the corresponding labels
       file_paths: numpy array
          Array with the paths of each image
    '''
    X = []
    y = []
    file_paths = []
    for folder in os.listdir(path):
        label = class_names_label[folder]
        folder_path = os.path.join(path, folder)
        for file in os.listdir(folder_path):
            image_path = os.path.join(folder_path, file)
            file_paths.append(image_path)
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, im_size)
            X.append(image)
            y.append(label)

    return np.array(X), np.array(y), np.array(file_paths)


def mapping(values, class_label_name):
    '''
    This function is used to map the predictions or the true labels from being labels on the food picture to be labels
    on the type of cuisine.

    Input:
    values : numpy array
        The array containings the labels (or predictions)
    class_label_names: dict
       A dictionary with integer index as keys and the names of the classes as values
    
    Output:
       true_finalLabels
          The new labels which refers to type of cuisine.
    '''
    italian_food = ["risotto", "pasta", "lasagna", "pizza"]
    japanese_food = ["tacos", "burrito", "nachos"]
    mexican_food = ["gyoza", "sushi", "edamame", "sashimi", "ramen"]

    true_finalLabel = []
    for elem in values:
        if class_label_name[elem] in italian_food:
            true_finalLabel.append("italian")
        elif class_label_name[elem] in mexican_food:
            true_finalLabel.append("mexican")
        elif class_label_name[elem] in japanese_food:
            true_finalLabel.append("japanese")
        else:
            print("ERROR for element at index", i)

    return true_finalLabel


