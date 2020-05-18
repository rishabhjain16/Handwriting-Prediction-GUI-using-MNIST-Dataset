from keras.models import load_model
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np

model = load_model('mnist.h5')

def digit_mnist_prediction(image):
    #resizing the image to 28x28 pixels
    image = image.resize((28,28))
    #convert the image to rgb to grayscale
    image = image.convert('L')
    image = np.array(image)
    #reshaping the image to support our model input and normalizing
    image = image.reshape(1,28,28,1)
    image = image/255.0
    #predicting the image class
    res = model.predict([image])[0]
    return np.argmax(res), max(res)

class GUI_App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.x = self.y = 0
        
        # Canvas creationg, buttons and labels
        self.canvas = tk.Canvas(self, width=300, height=300, bg = "white", cursor="cross")
        self.label = tk.Label(self, text="Draw here", font=("Arial", 48))
        self.predict_btn = tk.Button(self, text = "Predict", command = self.handwriting_prediction_model)   
        self.clear_btn = tk.Button(self, text = "Clear Workspace", command = self.clear_function)
       
        # Grid format for the GUI
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        self.label.grid(row=0, column=1,pady=2, padx=2)
        self.predict_btn.grid(row=1, column=1, pady=2, padx=2)
        self.clear_btn.grid(row=1, column=0, pady=2)
        
        self.canvas.bind("<B1-Motion>", self.drawing_cursor)

    def clear_function(self):
        self.canvas.delete("all")
        
    def handwriting_prediction_model(self):
        Handle = self.canvas.winfo_id()  #handle of the canvas
        rect = win32gui.GetWindowRect(Handle)  # coordinate of the canvas
        a,b,c,d = rect
        rect=(a+4,b+4,c-4,d-4)
        im = ImageGrab.grab(rect)

        digit, acc = digit_mnist_prediction(im)
        self.label.configure(text= str(digit)+', '+ str(int(acc*100))+'%')

    def drawing_cursor(self, event):
        self.x = event.x
        self.y = event.y
        r=8
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')
       
app = GUI_App()
app
mainloop()
