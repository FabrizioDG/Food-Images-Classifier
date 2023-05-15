## Convolutional Neural Network classifier for type of cuisines.

In this repository I present the results of a Machine Learning project I carried out at during the Data Science bootcamp at "The Bridge" school in Valencia (Spain). The aim of the project is to classify pictures of food through a convolutional neural network model, to recognize the type of cuisine of each picture.

### 1. Goals of the project
#### 1.1 Main objective

The aim of the project is to classify restaurants which appear on [TripAdvisor webpage](https://www.tripadvisor.com/Restaurants-g187529-Valencia_Province_of_Valencia_Valencian_Community.html) according to the type of cuisine proposed by the restaurant. In order to do that I propose a convolutional neural network classifier which takes as inputs pictures of different categories of food and it classify based on type of cuisine. Ideally this model could help to improve how the restaurants are labeled in the webpage.

At the moment the model is trained on 12 different food categories, corresponding to 3 different cuisines:
- risotto (Italian)
- pasta (Italian)
- pizza (Italian)
- lasagna (Italian)
- sushi (Japanese)
- sashimi (Japanese)
- ramen (Japanese)
- gyoza (Japanese)
- edamame (Japanese)
- tacos (Mexican)
- nachos (Mexican)
- burrito (Mexican)


### 2. Structure of the repository

#### 2.1 data folder

In this folder you can find the train and test set. Training set count around 26000 images, and test set around 1700 images. The test set is used as an external test, to evaluate the final accuracy of the model. Training set is instead divided in train and validation and it is used to train the model parameters. The dataset of pictures is a combination of pictures taken web-scraping from google images, tripadvisor webpage, and pinterest, plus pictures coming from public datasets as [Food 101](https://www.kaggle.com/datasets/dansbecker/food-101). The pictures obtained through webscraping are manually checked and most of the noisy picture have been removed.

#### 2.1 csv folder

In this folder you can find the csv files where I saved the urls of the pictures I obtained through webscraping

#### 2.2 src folder

This folder only contains a python script "functions.py", where I implemented a couple functions and where some global variables are stored.

#### 2.3 model folder

This folder contains some h5 files in which different models I tried have been saved. The file my_model.h5 is the one which gived me best accuracy on validation (around 0.66 accuracy).

#### 2.4 history folder

This folder contains the history of the training of some of the models I tried. The history file related to my_model.h5 is "history_model_64f5s_64f5ksame_128f3k_128f3k_d128n_12FoodClasses_BatchNorm_L2_tot.csv".

#### 2.5 notebooks folder

This folder contains the notebook where I implement the model architecture, its training and some analysis of the results:

