import tkinter as tk

class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.master.geometry("700x500")
        self.master.title('PyRIPg')

        self.grid(sticky=tk.N+tk.E+tk.S+tk.W, padx=4, pady=5)
        self.create_label()
        self.cr_spinbx()
        self.create_quit()
        #self.create_check()
        self.create_textbox()
        self.create_submit()

    def create_quit(self):
        self.quit = tk.Button(self,text="Quit",command=self.master.destroy,height=1)
        self.quit.grid(column=2, row=0, padx=10)

    def create_submit(self):
        self.bttn = tk.Button(self,text="Submit",command=self.get_subrddt,height=1)
        self.bttn.grid(column=0, row=2)


    def cr_spinbx(self):
        self.spinbx = tk.Spinbox(self,to=5000,from_=10,increment=10.0,width=4)
        self.spinbx.grid(column=1,row=0)

    def create_label(self):
        self.lbl1 = tk.Label(self,text="Photo Count", height=1)#,background='#D26F21')
        self.lbl1.grid(column=0,row=0)

        self.lbl2 = tk.Label(self,text="Subreddit", height=1)#,background='#D26F21')
        self.lbl2.grid(column=0,row=1)

    def create_check(self):
        self.num=tk.IntVar()

        CBttn = tk.Checkbutton(self,text="Option",variable=self.num, onvalue=1, offvalue=0,
                width=10)
        CBttn.grid(column=2,row=1)

    def create_textbox(self):
        self.Tbox = tk.Text(self,height=1,width=10)
        self.Tbox.grid(column=1,row=1)

    def get_subrddt(self):
        print(self.Tbox.get(0.0,tk.END),end="")

def main():
    root = tk.Tk()
    app = Window(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
