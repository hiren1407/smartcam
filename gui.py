from tkinter import *
from PIL import ImageTk, Image #import for JPEG PNG support
import tkinter as tk
from tkinter import font  as tkfont #import for fonts
import rf
import train as t

from tkinter import messagebox

# self is the master object used here
#Controller class for all frames
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("SmartCam")
        self.geometry("720x480")
        self.resizable(0, 0)
        self.iconbitmap('Images/favicon.ico')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (WelcomePage, SmartScan,AboutPage, Attendence, Inserts):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#front page
class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        load = Image.open("Images/nbg.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=1, y=1, relwidth=1, relheight=1)


        b2 = Button(self, height=2, width=40, text="Smart Scan",bg="#ffffff",activebackground = "#0077CC", bd=0.5,
                    command=lambda: controller.show_frame("SmartScan"))
        b2.place(relx=0.75,rely=0.42, anchor=CENTER)
        b3 = Button(self, height=2, width=40, text="About", bg="#ffffff", activebackground = "#0077CC",bd=0.5,
                    command=lambda: controller.show_frame("AboutPage"))
        b3.place(relx=0.75, rely=0.54, anchor=CENTER)
        b4 = Button(self, height=2, width=40, text="Exit", bg="#ffffff", activebackground = "#0077CC",bd=0.5,
                    command=self.quit)
        b4.place(relx=0.75, rely=0.66, anchor=CENTER)

#Main function page
class SmartScan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def fun():
            rf.run()

        # img is background image
        load = Image.open("Images/bg4.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=1, y=1, relwidth=1, relheight=1)

        # b3 is button used
        b2 = Button(self, height=2, width=20, text="Start Attendence", bg="#ffffff", activebackground = "#0077CC",bd=2,
                    command=lambda: [f() for f in [lambda: controller.show_frame("Attendence"), fun]])
        b2.place(relx=0.35, rely=0.8, anchor=CENTER)
        b3 = Button(self, height=2, width=20, text="Enroll New Faculty", bg="#ffffff",activebackground = "#0077CC", bd=2 , 
                    command=lambda: controller.show_frame("Inserts"))
        b3.place(relx=0.65, rely=0.8, anchor=CENTER )
        b4 = Button(self, height=1, width=7, text="Back",activebackground = "#0077CC", bg="#ffffff", bd=0,
                    command=lambda: controller.show_frame("WelcomePage"))
        b4.place(relx=0.07, rely=0.06, anchor=CENTER)



#attendence page
class Attendence(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # img is background image
        load = Image.open("Images/bg3.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=1, y=1, relwidth=1, relheight=1)

        # b3 is button used
        b3 = Button(self, height=2, width=20, text="Stop Attendence",activebackground = "#0077CC", bg="#ffffff", bd=2,
                    command=lambda: controller.show_frame("WelcomePage"))
        b3.place(relx=0.5, rely=0.9 , anchor=CENTER)



#about page
class AboutPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # img is background image
        load = Image.open("Images/bg2.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=1, y=1, relwidth=1, relheight=1)

        b2 = Button(self, height=1, width=7, text="Back",activebackground = "#0077CC", bg="#ffffff", bd=0,
                    command=lambda: controller.show_frame("WelcomePage"))
        b2.place(relx=0.07, rely=0.06, anchor=CENTER)

class Inserts(tk.Frame):

     

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        load = Image.open("Images/raw.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=1, y=1, relwidth=1, relheight=1)
        message = tk.Label(self, text="Enroll New Faculty" ,justify = CENTER , width=40  ,height=2,font=('Hetelvica', 16,'bold' )) 

        message.place(relx=.16, rely=.0185)

        lbl = tk.Label(self, text="Enter Faculty Id -",width=13, justify = LEFT  ,height=1 ,font=('Hetelvica', 12 , 'bold' ) ) 
        lbl.place(relx=0.1, rely=0.185)

        txt = tk.Entry(self,width=35 ,font=('Hetelvica', 12 ))
        txt.place(relx=0.364, rely=0.185)
        

        lbl2 = tk.Label(self, text="Enter Name -",width=13  ,height=1 ,font=('Hetelvica', 12, 'bold' )) 
        lbl2.place(relx=0.1, rely=0.327)

        txt2 = tk.Entry(self,width=35 ,font=('Hetelvica', 12 ))
        txt2.place(relx=0.364, rely=0.327)

        lbl3 = tk.Label(self, text="Notification -",width=13   ,height=1 ,font=('Hetelvica', 12 , 'bold' )) 
        lbl3.place(relx=0.1, rely=0.4703)

        var=StringVar()
        message = tk.Label(self, textvariable=var ,width=35  ,height=1,font=('Hetelvica', 12 )) 
        message.place(relx=0.364, rely=0.4703)


 
        def clear():
            var.set("")
            txt.delete(0, 'end')    
            res = ""
            message.configure(text= res)
            txt2.delete(0, 'end')    
            res = ""
            message.configure(text= res) 
            


        def TakeImage():        
            rollNo=(txt.get())
            name=(txt2.get())
            if rollNo=="" or name=="":
                var.set("Please enter your details first ")
            elif not rollNo.isdigit():
                var.set("Please enter valid faculty id")
            elif not all(x.isalpha() or x.isspace() for x in name):
                var.set("Please enter valid name")
            else:
                msg=t.run(name,rollNo)
                var.set(msg)
            

            



        clearButton = tk.Button(self, text="Clear", command=clear  ,width=7  ,height=1 ,activebackground = "#0077CC" ,font=('Hetelvica', 12 , 'bold'))
        clearButton.place(relx=0.83, rely=0.245 )
   
        takeImg = tk.Button(self, text="Take Image" ,command=TakeImage ,width=20  ,height=2, activebackground = "#0077CC" ,font=('Hetelvica', 12 , 'bold'))
        takeImg.place(relx=0.5, rely=0.8, anchor=CENTER)

        back = Button(self, height=1, width=7, text="Back",activebackground = "#0077CC", bg="#ffffff", bd=0,
                    command=lambda: controller.show_frame("SmartScan"))
        back.place(relx=0.07, rely=0.06, anchor=CENTER)




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

