# Handwriting-Prediction-GUI-using-MNIST-Dataset

The handwritten digit recognition is the ability of computers to recognize human handwritten digits. It is a hard task for the machine because handwritten digits are not perfect and can be made with many different flavors. The handwritten digit recognition is the solution to this problem which uses the image of a digit and recognizes the digit present in the image.

Make sure you have Python 3.x setup on your operating system.

## Prerequisites before using this software :

Install the follow libraries to meet the dependencies :
1. Tensorflow
2. Keras
3. Pillow
4. The supporting libraries like numpy,pil and all others (which are automatically installed while installing the above mentioned libraries)

## The MNIST dataset
This is probably one of the most popular datasets among machine learning and deep learning enthusiasts. The MNIST dataset contains 60,000 training images of handwritten digits from zero to nine and 10,000 images for testing. So, the MNIST dataset has 10 different classes. The handwritten digits images are represented as a 28×28 matrix where each cell contains grayscale pixel value.

## Compiling and Running
Put all the files in single folder and run Digit_prediction_GUI_MNIST.py using python or CMD
Example: python3 Digit_prediction_GUI_MNIST.py


## Building Python Deep Learning Project on Handwritten Digit Recognition

1. Import the libraries and load the dataset - First, we are going to import all the modules that we are going to need for training our model. The Keras library already contains some datasets and MNIST is one of them. So we can easily import the dataset and start working with it. The mnist.load_data() method returns us the training data, its labels and also the testing data and its labels.

2. Preprocess the data - The image data cannot be fed directly into the model so we need to perform some operations and process the data to make it ready for our neural network. The dimension of the training data is (60000,28,28). The CNN model will require one more dimension so we reshape the matrix to shape (60000,28,28,1).

3. Create the model - Now we will create our CNN model in Python data science project. A CNN model generally consists of convolutional and pooling layers. It works better for data that are represented as grid structures, this is the reason why CNN works well for image classification problems. The dropout layer is used to deactivate some of the neurons and while training, it reduces offer fitting of the model. We will then compile the model with the Adadelta optimizer.

4. Train the model - The model.fit() function of Keras will start the training of the model. It takes the training data, validation data, epochs, and batch size. It takes some time to train the model. After training, we save the weights and model definition in the ‘mnist.h5’ file.

5. Evaluate the model - We have 10,000 images in our dataset which will be used to evaluate how good our model works. The testing data was not involved in the training of the data therefore, it is new data for our model. The MNIST dataset is well balanced so we can get around 99% accuracy.

6. Create GUI to predict digits - Now for the GUI, we have created a new file in which we build an interactive window to draw digits on canvas and with a button, we can recognize the digit. The Tkinter library comes in the Python standard library. We have created a function digit_mnist_prediction() that takes the image as input and then uses the trained model to predict the digit.

## References and Acknowledgement:
1. https://data-flair.training/

## Example Images:
![Example 1 - Predicting number 2](https://github.com/rishabhjain16/Handwriting-Prediction-GUI-using-MNIST-Dataset/blob/master/Example%201.PNG)
![Example 2 - Predicting number 8](https://github.com/rishabhjain16/Handwriting-Prediction-GUI-using-MNIST-Dataset/blob/master/Example%202.PNG)
![Example 3 - Predicting number 7](https://github.com/rishabhjain16/Handwriting-Prediction-GUI-using-MNIST-Dataset/blob/master/Example%204.PNG)
