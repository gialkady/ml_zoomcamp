## Best restaurant to serve
![img](https://github.com/gialkady/ml_zoomcamp/blob/Homeworks/Capstone%20Project/images/istockphoto-531306158-612x612.jpeg)


## overview 

This project is done as part of the Machine Learning course held by Alexey Grigorev.


## Idea (Problem Description)

How many times you saw a food image on the internet and you feel that you want to eat it NOW 🤩 😉  

In this project, we tried to make your dreams come true. The idea is a web service that help people to know the best restaurant to serve the food dish on an image on their city. 

- Firstly, the user upload the food image
- ML engine based on deep learning will classify the image (food class). 
- According to the class of food, the system will response with the name of the best restaurant to serve the dish in the user's city.

![img](https://github.com/gialkady/ml_zoomcamp/blob/Homeworks/Capstone%20Project/images/Best%20Restaurant%20to%20serve.png)

## Dataset

The dataset used in this project is Food-101 dataset (https://www.kaggle.com/kmader/food41)

Food-101 is a dataset consisting of 101 food classes with 1000 images per class. For each class, 250 images are reserved as for the test set and the rest 750 images for training (80% train, 20% val). In the directory food-101 we find a folder with images and one with meta information. The images folder contains 101 folders with 1000 images each. Each folder contains images of a specific food class while the meta folder contain the information tells us what the train and test (validation) images are.

**meta** folder contains the text files - train.txt and test.txt  
**train.txt** contains the list of images that belong to training set  
**test.txt** contains the list of images that belong to test set  
**classes.txt** contains the list of all classes of food

**Problems in dataset**

- Small amount of training data for each class
- Many classes look similar to each other (steak vs filet mignon)
- Many images in the dataset have poor lighting or framing.
- Several images contain multiple correct classes (ex burgers & fries)
- Number of mislabeled images.
- Image shapes vary within class

Most of the dataset problems can be solved through applying "Image augmentation".

![img] (https://github.com/gialkady/ml_zoomcamp/blob/Homeworks/Capstone%20Project/images/Screen%20Shot%202021-12-13%20at%2010.57.25%20PM.png)

## 







