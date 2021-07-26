from tkinter import *
from tkinter.ttk import *

import sophia



window = Tk()
window.geometry("500x500")
window.configure(bg='#8FCACA')
window.title("SOFIA")

def call():
    sophia.work()

def close():
    window.destroy()


#label = Label(window, text="SOFIA!\nIn your Service!", font=("Verdana", 10)).pack(side=TOP)

#frame = Frame(window)
#scrollbar = Scrollbar(frame)
#msg = Listbox(frame,bg='#F5EAC2',bd=0,height=28,width=80,yscrollcommand=scrollbar.set)
#scrollbar.pack(side=RIGHT,fill=Y)
#msg.pack(side=LEFT,fill=BOTH)
#msg.pack()
#frame.pack()

photo0 = PhotoImage(file=r"C:\Users\ASUS\OneDrive\Desktop\Projects\pythonProject\Sophia\logo2.png")
pic0 = photo0.subsample(2,2)
mic_widget0 = Button(window,image=pic0, compound=RIGHT).pack()
photo1 = PhotoImage(file=r"C:\Users\ASUS\OneDrive\Desktop\Projects\pythonProject\Sophia\mic.png")
pic1 = photo1.subsample(14, 14)
photo2 = PhotoImage(file=r"C:\Users\ASUS\OneDrive\Desktop\Projects\pythonProject\Sophia\close.png")
pic2 = photo2.subsample(14, 14)
mic_widget1 = Button(window,image=pic1, compound=RIGHT, command =call).pack(side=LEFT,anchor=S)
mic_widget2 = Button(window, image=pic2, compound=LEFT, command=close).pack(side=RIGHT,anchor=S)




window.mainloop()



