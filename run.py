import tkinter as tk
import csv
import numpy as np
from exercise import *
import random

root = tk.Tk()
root.title("Test Window")
root.geometry("400x400")
root.resizable(False, False)

SQUARE_UNIT = 400/28

display_grid = tk.Canvas(root, bg="black", width=400, height=400, relief="raised")
display_grid.place(x=0, y=0)

squares = []
for y in range(28):
    for x in range(28):
        square = display_grid.create_rectangle(x*SQUARE_UNIT,
         y*SQUARE_UNIT, 
         (x+1)*SQUARE_UNIT, 
         (y+1)*SQUARE_UNIT, 
         fill="Black")
         
        squares.append(square)

train_set = np.loadtxt('data/mnist_train_800.csv', delimiter=',', skiprows=1)
classifier = Classifier(10)

accuracy = classifier.train(train_set, 100)

accuracy_label = tk.Label(root,
               text=f"Train Accuracy: {accuracy}%",
               font=("Arial", 10),
               bg="black",
               fg="white",
               width=20,
               height=2,
               relief="flat")
accuracy_label.place(x=2, y=2)

test_set = np.loadtxt('data/mnist_test_200.csv', delimiter=',', skiprows=1)

def show_number(number):
    for i in range(784):
        gray = number[i]
        hex_color = f"#{int(gray):02x}{int(gray):02x}{int(gray):02x}"

        display_grid.itemconfig(squares[i], fill=hex_color)

show_number(test_set[0])

answer_label = tk.Label(root,
               text=4,
               font=("Arial", 10),
               bg="black",
               fg="white",
               width=20,
               height=2,
               relief="flat")
answer_label.place(x=300, y=2)

def classify_number():
    number = random.choice(test_set)
    show_number(number)
    predicted = classifier.classify(number)
    color = 'red'
    if (predicted == number[-1]):
        color = "spring green"
    answer_label.config(text=predicted, fg=color)
    
classify_button = tk.Button(root, 
                text="Classify",
                bd = 0,
                command=classify_number, 
                font=("Arial", 10),
                bg="black",
                fg="white",
                width=5,
                height=2,
                relief="flat")
classify_button.place(x=0, y=353)

root.mainloop()