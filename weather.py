from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


root = Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)


##icon
image_icon=PhotoImage(file="iimages/logo.png")
root.iconphoto(False,image_icon)

#print(os.getcwd())




root.mainloop()