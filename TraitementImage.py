import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import *
from pathlib import Path
from glob import glob
import random
from PIL import Image
from PIL import ImageTk
import cv2
from tkinter import filedialog
from tkinter import ttk


index = ["color_name", "B", "G", "R"]
csv = pd.read_csv('couleur.csv', names=index, header=None)
def getColorName(B, G, R):
    minimum = 1000
    for i in range(len(csv)):
        d = abs(B - int(csv.loc[i, "B"])) + abs(G - int(csv.loc[i, "G"])) + abs(R - int(csv.loc[i, "R"]))
        if (d <= minimum):
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

def getRGB(color):
    a=list()
    for i in range(len(csv)):
        if csv.loc[i, "color_name"]==color:
            a.extend([int(csv.loc[i, "B"]),int(csv.loc[i, "G"]),int(csv.loc[i, "R"])])
            break
    return a

def color_detection(im):
    colors={}

    for i in range(len(im)):
        for j in range(len(im[i])):
            colors.setdefault((i,j), getColorName(int(im[i][j][0]),int(im[i][j][1]),int(im[i][j][2])))
    return colors

def get_keys_from_value(d, color):
    return [k for k, v in d.items() if v == color]


def changer_color(liste,bgr):
    for v in liste:
        img[v[0]][v[1]]=getRGB(bgr)
def afficher_colors(colors):
    return set(colors.values())






def inter1() :
    root = tk.Tk()
    root.geometry("800x700")
    canvas = tk.Canvas(root, height=200, width=200)
    filename = PhotoImage(file='fondo.png')
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    canvas.pack()
    button_show = tk.Button(root, text="Start ", bg="#BFFF33", fg="black", width=20, command = lambda:[root.destroy(),inter3()])
    button_show.pack()
    button_show.place(relx=0.4, rely=0.5)
    root.mainloop()


def inter3() :
    def insertion():
        global panelA, img, PanelB
        path = filedialog.askopenfilename()
        if len(path) > 0:
            # load the image from disk
            image = cv2.imread(path)
            img = image
            image = cv2.resize(image, (640, 560))
            # OpenCV represents images in BGR order; however PIL represents
            # images in RGB order, so we need to swap the channels
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # convert the images to PIL format...
            image = Image.fromarray(image)
            # ...and then to ImageTk format
            image = ImageTk.PhotoImage(image)
            if panelA is None:
                # the first panel will store our original image

                panelA = Label(image=image)
                panelA.image = image
                panelA.place(relx=0.3, rely=0.1)
                #panelA.pack(side="top-right")
            else:
                panelA.configure(image=image)

                panelA.image = image


    root = tk.Tk()


    canvas = tk.Canvas(root, height=700, width=800)
    filename = PhotoImage(file='fondo.png')
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    canvas.pack()

    frame1 = tk.Frame(root)
    frame1.place(rely=0.2, relwidth=0.2, relheight=0.4)
    filename2 = PhotoImage(file='fondo.png')
    background_label = Label(frame1, image=filename2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame2 = tk.Frame(root)
    frame2.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

    button_show = tk.Button(frame1, text="Inserer une image ", bg="#BFFF33", fg="black",width = 16, command=insertion)
    button_show.pack()
    button_show.place(relx=0.1, rely=0.1)

    button_show = tk.Button(frame1, text="Couleurs de l'image ",bg="#BFFF33", fg="black",width = 16, command = lambda  : [root.destroy(),inter_clr()])
    button_show.pack()
    button_show.place(relx=0.1, rely=0.4)

    button_change = tk.Button(frame1, text="Changer une couleur", bg="#BFFF33", fg="black",width = 16,command =lambda :[root.destroy(),changer_clr()])
    button_change.pack()
    button_change.place(relx=0.1, rely=0.7)
    root.mainloop()

def inter_clr() :
    im = list(afficher_colors(color_detection(img)))

    def structurer(frame):
        for i in im:
            # text = Label(frame, text=i, fg="black",bg="red", font=("Red Hat Mono", 11))
            Button(frame, text=i, command=None,bg=i).pack(padx=5, pady=5)
   
    root = tk.Tk()

    canvas = tk.Canvas(root, height=700, width=800)
    filename = PhotoImage(file='fondo.png')
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    canvas.pack()

    frame1 = tk.Frame(root)
    frame1.place(rely=0.2, relwidth=0.2, relheight=0.4)
    filename2 = PhotoImage(file='fondo.png')
    background_label = Label(frame1, image=filename2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame2 = tk.Frame(root)
    frame2.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

    button_insert = tk.Button(frame1, text="Inserer une image ", bg="#BFFF33",width = 16, fg="black")
    button_insert.pack()
    button_insert.place(relx=0.1, rely=0.1)

    button_show = tk.Button(frame1, text="Couleurs de l'image ", bg="#BFFF33", fg="black",width = 16,command=lambda: [root.destroy(), inter_clr()])
    button_show.pack()
    button_show.place(relx=0.1, rely=0.4)

    button_change = tk.Button(frame1, text="Changer une couleur", bg="#BFFF33", fg="black",width = 16,command = lambda :[root.destroy(),changer_clr()])
    button_change.pack()
    button_change.place(relx=0.1, rely=0.7)
    structurer(frame2)
    root.mainloop()


def changer_clr():


    root = tk.Tk()

    canvas = tk.Canvas(root, height=700, width=800)
    filename = PhotoImage(file='fondo.png')
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    canvas.pack()

    frame1 = tk.Frame(root)
    frame1.place(rely=0.2, relwidth=0.2, relheight=0.4)
    filename2 = PhotoImage(file='fondo.png')
    background_label = Label(frame1, image=filename2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame2 = tk.Frame(root)
    frame2.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)
    clr1=StringVar(frame1)
    clr2 = StringVar(frame1)

    label_d = Label(frame1, text="La couleur à changer : ")
    label_d.pack()
    label_d.place(rely = 0.1)

    name1 = Entry(frame1,textvariable=clr1)
    name1.focus_set()
    name1.pack()
    name1.place(relx=0.1,rely = 0.3)

    label_i = Label(frame1, text="Couleur à mettre :")
    label_i.pack()
    label_i.place(rely = 0.5)

    name2 = Entry(frame1,textvariable=clr2)
    name2.focus_set()
    name2.pack()
    name2.place(relx = 0.1,rely = 0.7)
    button_change = tk.Button(frame1, text="Commencer", bg="#BFFF33", fg="black",width = 16, command = lambda : [root.destroy(),changer_color(get_keys_from_value(color_detection(img), clr1.get()), clr2.get()),final_show()])
    button_change.pack()
    button_change.place(relx=0.1, rely=0.9)
    root.mainloop()


def final_show():
    def nv_show(img):
        pic = cv2.resize(img, (640, 560))
        pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
        pic = Image.fromarray(pic)
        pic = ImageTk.PhotoImage(pic)
        panelB = Label(image=pic)
        panelB.image = pic
        panelB.place(relx=0.3, rely=0.1)
        #panelB.pack(side="top-right")


    def save() :
        result = filedialog.asksaveasfilename(initialdir="/", title="Select file", initialfile = img ,filetypes=(
            ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif')))


    root = tk.Tk()

    canvas = tk.Canvas(root, height=700, width=800)
    filename = PhotoImage(file='fondo.png')
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    canvas.pack()

    frame1 = tk.Frame(root)
    frame1.place(rely=0.2, relwidth=0.2, relheight=0.4)
    filename2 = PhotoImage(file='fondo.png')
    background_label = Label(frame1, image=filename2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame2 = tk.Frame(root)
    frame2.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)
    button_change = tk.Button(frame1, text="Afficher", bg="#BFFF33", fg="black",width = 16, command = lambda :[nv_show(img)])
    button_change.pack()
    button_change.place(relx=0.1, rely=0.5)

    root.mainloop()



# to display the image in the inter3
panelA =panelB= None
img = None
inter1()