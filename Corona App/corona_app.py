def Scrap():
    def notifyme(title,message):
        plyer.notification.notify(
            title = title,
            message = message
            app_icon = "C:\\Personal Files\\Ishan\\Python\\Corona App\\icon.ico"
            timeout = 30
        )
    url = 'https://www.worldometers.info/coronavirus'
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    tablebody = soup.find('tbody')
    ttt = tablebody.find_all('tr')
    notifycountry = corntrydata.get()
    if(notifycountry == ''):
        notifycountry = 'india'
    countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases, serious, totalcases_permillion, totaldeaths_permillion, totaltests, totaltests_permillion = [], [], [], [], [], [], [], [], [], [], [], []
    headers = ['Countries', 'Total Cases', 'New Cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'Active Cases', 'Serious', 'total Cases per Million', 'Total Deaths per Million', 'Total Tests', 'Total Tests per Million']

    for i in ttt:
        id = i.find_all('td')
        if(id[0].text.strip().lower() == notifycountry):
            

from bs4 import BeautifulSoup
import plyer
import requests
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import pandas as pd
import webbrowser as wb
from tkinter import *



root = Tk()
root.title("Corona Virus information")
root.geometry("760x450+200+80")
root.resizable(45, 45)
formatlist = []

bagi = Image.open("C:\\Files\\Ishan\\Python\\Corona App\\corona.jpg")
bag = ImageTk.PhotoImage(bagi)


label = Label(root,bagi = bag,background = "white")
label.place(x = 0, y = 0)

Introlabel = Label(root,text = 'Corona Virus Information',font = ('New roman', 30, 'italic bold'), bg = '#ff9900', width = 32)
Introlabel.place(x = 0, y = 0)

Entrylabel = Label(root,text = 'Choose your country :',font = ('arial', 18, 'bold'), bg = '#339966', fg = 'white')
Entrylabel.place(x = 10, y = 160)

Formatlabel = Label(root,text = 'Download all country :',font = ('arial', 18, 'bold'), bg = '#339966', fg = 'white')
Formatlabel.place(x = 10, y = 250)

countrydata = StringVar()
ent1 = Entry(root, textvariable = countrydata, font = ('arial', 18, 'italic bold'), bd = 4)
ent1.place(x = 350, y = 160)

def open_window():
    top = Toplevel()
    top.geometry("100x100 + 350 + 250")
    wb.open_new(r"C:\\Files\\Ishan\\Python\\Corona App\\info.pdf")


InJson = Button(root,text = 'Excel',width = 7, fg ="white", bg = "#9900cc",font = ('arial', 13, 'bold'),relief = RIDGE,
                activebackground = 'green', activeforeground = 'white', command = incsv)
InJson.place(x = 390,y = 250)

InHtml = Button(root,text = 'Html',width = 7, fg ="white", bg = "#9900cc",font = ('arial', 13, 'bold'),relief = RIDGE,
                activebackground = 'green', activeforeground = 'white', command = inhtml)
InHtml.place(x = 390,y = 250)

submit = Button(root,text = 'Submit',width = 13, bg = "#ff3300",font=('arial', 17,'italic bold'),
            activebackground = 'green', activeforeground = 'white', command = download)
submit.place(x = 350, y = 390)

Infor = Button(root,text = 'Info',width = 13, bg = "#00ff00",font=('arial', 17,'italic bold'),
            activebackground = '#00ff00', command = open_window)
Infor.place(x = 130, y = 390)



root.mainloop()