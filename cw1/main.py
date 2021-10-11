import tkinter



def window():
    root = tkinter.Tk()
    root.iconbitmap("copy.bmp")

    Imie = tkinter.StringVar()
    Imie.set("Mateusz")
    Nazwisko = tkinter.StringVar()
    Nazwisko.set("Maliszewski")


    root.title("3Tpgr2")
    root.geometry("400x400")
    root.resizable(False, False)
    l1 = tkinter.Label(root, textvariable=Imie, bg="black",fg="white", font=("Times New Roman", 16, "italic"))
    l1.grid(row=0, column=0)
    l2 = tkinter.Label(root, textvariable=Nazwisko, bg="#000000",fg="#ffffff", font=("Arial", 16, "bold"))
    l2.grid(row=1, column=0)

    root.mainloop()




if __name__ == "__main__":
    window()