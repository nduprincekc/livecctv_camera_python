from tkinter import *
from PIL import Image,ImageTk
from record import record


window = Tk()
window.title('Live CCTV CAMERA')
window.iconphoto(False,PhotoImage(file='eeeee.png'))
window.geometry('1080x600')


# main Frame
mainframe = Frame(window,bd=2)

label_title =Label(mainframe,text = 'LIVE  CCTV CAMERA',font=('Helivca',22,'bold'))
label_title.grid(pady=10,padx=10,column=1,row=0)

icon_1 = Image.open('img_1.png')
icon_1 = icon_1.resize((70,70),Image.ANTIALIAS)
icon_1 = ImageTk.PhotoImage(icon_1)
label_icon = Label(mainframe,image=icon_1)
label_icon.grid(row=0,pady=(5,10),column = 0)




icon_spy = Image.open('img.png')
icon_spy = icon_spy.resize((100,100),Image.ANTIALIAS)
icon_spy = ImageTk.PhotoImage(icon_spy)
label_icon = Label(mainframe,image=icon_spy)
label_icon.grid(row=3,pady=(10),column = 1)



btn_image =  Image.open('img_1.png')
btn_image = btn_image.resize((50,50),Image.ANTIALIAS)
btn_image = ImageTk.PhotoImage(btn_image)


btn =Button(mainframe,text='VIDEO RECORD',command =record ,font=('Helvetica',25,'bold'),height=90,width=300,fg='orange',image=btn_image,compound='left')
btn.grid(row=5,pady=(20,10),column=1)



# exist button

btn_image1 =  Image.open('img_1.png')
btn_image2 = btn_image1.resize((50,50),Image.ANTIALIAS)
btn_image2 = ImageTk.PhotoImage(btn_image1)


btn1 =Button(mainframe,text='EXIT',font=('Helvetica',25,'bold'),height=90,width=300,fg='orange',image=btn_image,compound='left')
btn1.grid(row=6,pady=(20,10),column=1)




















mainframe.pack()






window.mainloop()
