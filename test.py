import tkinter

window = tkinter.Tk()

window.title("Tkinter Test")
window.geometry("640x400+100+100")
window.resizable(False, False)

# 라벨1
text = "Python Tkinter Test"
width = 100
height = 3
fg = "black"
relief = "ridge"

label = tkinter.Label(window, 
                      text=text,
                      width=width,
                      height=height,
                      fg=fg,
                      relief=relief
                      )
label.pack()

window.mainloop()
