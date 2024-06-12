from tkinter import *
window = Tk()
window.geometry('900x600')#for width and height
#png , gif file mattum than tkinter la work agum
#first image view panrathuku first image ah load pannanum
reg_img = PhotoImage(file= '')
#image view pannanum na athuku first nama oru label create pannanum
bg_label = Label(window, image=reg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
window.mainloop()  #mainloop runs for compelete program run pannum,kandipa main loop kuduthe aganum