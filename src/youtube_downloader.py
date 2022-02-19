from tkinter import *
from pytube import YouTube
from PIL import Image,ImageTk
def download_():
    
    url = entry_link.get()
    my_video = YouTube(url)
    
    last_choice= format_choice.get()
    
    if last_choice == 1:
        my_video.streams.get_highest_resolution().download()

    elif last_choice == 0:
        my_video.streams.get_audio_only().download()
    else:
        pass

root = Tk()
canvas = Canvas(root,height=300,width=500)
canvas.pack()
title = root.title("My Youtube Downloader")
logo = Image.open("C:/Users/benim/desktop/youtube/logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image=logo
logo_label.place(relx=0.2,rely=0.15)
entry_label = Label(root,text="Url",font=("Permanent Marker",16))
entry_label.place(relx=0.1,rely=0.4)
entry_link = Entry(root,width=48) 
entry_link.place(relx=0.2,rely=0.43)
confirm_btn = Button(root,text="Download",command=lambda:download_(),font=("Permanent Marker",14),bg="#05a4f7")
confirm_btn.place(relx=0.4,rely=0.7)
inform_label = Label(root,text="Lütfen kopyaladığınız linki yapıştırın...",font=("Permanent Marker",12))
inform_label.place(relx=0.18,rely=0.52)
format_choice = IntVar()
btn_selcetion1 = Radiobutton(root,text="Mp3 ",variable=format_choice,value=0,font=("Permanent Marker",10),bg="#05a4f7")
btn_selcetion1.place(relx=0.8,rely=0.38)
btn_selcetion2 = Radiobutton(root,text="Video",variable=format_choice,value=1,font=("Permanent Marker",10),bg="#05a4f7")
btn_selcetion2.place(relx=0.8,rely=0.5)
root.mainloop()
















